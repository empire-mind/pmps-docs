import json
import sqlite3
from pathlib import Path

SCHEMA = (
    "CREATE TABLE IF NOT EXISTS events ("
    "sequence INTEGER PRIMARY KEY AUTOINCREMENT,"
    "event_id TEXT UNIQUE NOT NULL,record_id TEXT NOT NULL,"
    "event_type TEXT NOT NULL,occurred_at TEXT NOT NULL,payload TEXT NOT NULL);"
)

class Ledger:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute(SCHEMA)

    def append(self, event: dict) -> None:
        self.db.execute(
            "INSERT INTO events(event_id,record_id,event_type,occurred_at,payload)"
            " VALUES(?,?,?,?,?)",
            (event["event_id"], event["record_id"], event["event_type"],
             event["occurred_at"], json.dumps(event, sort_keys=True)),
        )
        self.db.commit()

    def replay(self, record_id: str) -> list[dict]:
        rows = self.db.execute(
            "SELECT payload FROM events WHERE record_id=? ORDER BY sequence",
            (record_id,),
        ).fetchall()
        return [json.loads(row[0]) for row in rows]

    def close(self) -> None:
        self.db.close()
