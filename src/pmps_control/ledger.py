"""Append-only, hash-chained control ledger."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any


GENESIS_HASH = "0" * 64

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT UNIQUE NOT NULL,
    record_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    content_sha256 TEXT,
    event_hash TEXT NOT NULL,
    prev_hash TEXT,
    payload TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_events_record_id ON events(record_id);
CREATE INDEX IF NOT EXISTS idx_events_content_sha256 ON events(content_sha256);
"""


def _event_hash(event: dict[str, Any], prev_hash: str) -> str:
    """Hash event body + previous hash for tamper evidence."""
    body = {
        "event_id": event["event_id"],
        "record_id": event["record_id"],
        "event_type": event["event_type"],
        "occurred_at": event["occurred_at"],
        "payload": event,
        "prev_hash": prev_hash,
    }
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class Ledger:
    def __init__(self, path: Path | str):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self._db: sqlite3.Connection | None = sqlite3.connect(path)
        self._db.row_factory = sqlite3.Row
        self._db.executescript(SCHEMA)
        self._db.commit()

    @property
    def db(self) -> sqlite3.Connection:
        if self._db is None:
            raise RuntimeError("Ledger is closed")
        return self._db

    def __enter__(self) -> "Ledger":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def close(self) -> None:
        if self._db is not None:
            self._db.close()
            self._db = None

    def _latest_hash(self) -> str:
        row = self.db.execute(
            "SELECT event_hash FROM events ORDER BY sequence DESC LIMIT 1"
        ).fetchone()
        return row["event_hash"] if row else GENESIS_HASH

    def append(self, event: dict[str, Any]) -> dict[str, Any]:
        return self.append_many([event])[0]

    def append_many(self, events: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not events:
            return []
        prev_hash = self._latest_hash()
        enriched: list[dict[str, Any]] = []
        try:
            for event in events:
                event = dict(event)
                content_sha = event.get("sha256")
                event_hash = _event_hash(event, prev_hash)
                event["prev_hash"] = prev_hash
                event["event_hash"] = event_hash
                self.db.execute(
                    "INSERT INTO events("
                    "event_id, record_id, event_type, occurred_at, "
                    "content_sha256, event_hash, prev_hash, payload"
                    ") VALUES(?,?,?,?,?,?,?,?)",
                    (
                        event["event_id"],
                        event["record_id"],
                        event["event_type"],
                        event["occurred_at"],
                        content_sha,
                        event_hash,
                        prev_hash,
                        json.dumps(event, sort_keys=True),
                    ),
                )
                enriched.append(event)
                prev_hash = event_hash
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        return enriched

    def replay(self, record_id: str) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT payload FROM events WHERE record_id=? ORDER BY sequence",
            (record_id,),
        ).fetchall()
        return [json.loads(row["payload"]) for row in rows]

    def find_by_content_hash(self, content_sha256: str) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT payload FROM events "
            "WHERE content_sha256=? AND event_type='record.received' "
            "ORDER BY sequence",
            (content_sha256,),
        ).fetchall()
        return [json.loads(row["payload"]) for row in rows]

    def verify_chain(self) -> dict[str, Any]:
        rows = self.db.execute(
            "SELECT sequence, event_hash, prev_hash, payload "
            "FROM events ORDER BY sequence"
        ).fetchall()
        prev = GENESIS_HASH
        for row in rows:
            try:
                payload = json.loads(row["payload"])
                body = {
                    k: v
                    for k, v in payload.items()
                    if k not in ("event_hash", "prev_hash")
                }
                if row["prev_hash"] != prev:
                    return {
                        "ok": False,
                        "checked": int(row["sequence"]) - 1,
                        "first_bad_sequence": int(row["sequence"]),
                        "reason": "prev_hash_mismatch",
                    }
                recomputed = _event_hash(body, prev)
                if recomputed != row["event_hash"]:
                    return {
                        "ok": False,
                        "checked": int(row["sequence"]) - 1,
                        "first_bad_sequence": int(row["sequence"]),
                        "reason": "event_hash_mismatch",
                    }
            except (KeyError, TypeError, json.JSONDecodeError):
                return {
                    "ok": False,
                    "checked": int(row["sequence"]) - 1,
                    "first_bad_sequence": int(row["sequence"]),
                    "reason": "corrupt_payload",
                }
            prev = row["event_hash"]
        return {"ok": True, "checked": len(rows), "tip_hash": prev}
