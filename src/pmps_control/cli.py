"""CLI for PMPS document control."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from .ledger import Ledger
from .runtime import intake, record_approval


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pmps-control")
    parser.add_argument("--config", type=Path, default=Path("config/runtime.yaml"))
    parser.add_argument(
        "--ledger", type=Path, default=Path("data/control-ledger.sqlite3")
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("intake", help="Fingerprint and route a source file")
    add.add_argument("source", type=Path)
    add.add_argument("--metadata", type=Path, required=True)
    add.add_argument("--confidence", type=float, required=True)

    replay = commands.add_parser("replay", help="Replay ledger events for a record")
    replay.add_argument("record_id")

    approve = commands.add_parser(
        "approve", help="Record human approval bound to content hash"
    )
    approve.add_argument("record_id")
    approve.add_argument("--decision", required=True, choices=["APPROVED", "REJECTED"])
    approve.add_argument("--approver", required=True)
    approve.add_argument("--sha256", required=True)
    approve.add_argument("--version", required=True)
    approve.add_argument("--document-id", default=None)

    commands.add_parser("verify", help="Verify ledger hash chain")

    args = parser.parse_args(argv)

    with Ledger(args.ledger) as ledger:
        if args.command == "replay":
            result: object = ledger.replay(args.record_id)
        elif args.command == "verify":
            result = ledger.verify_chain()
        elif args.command == "approve":
            config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
            result = record_approval(
                args.record_id,
                decision=args.decision,
                approver=args.approver,
                content_hash=args.sha256,
                version=args.version,
                config=config,
                ledger=ledger,
                document_id=args.document_id,
            )
        else:
            config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
            metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
            result = intake(
                args.source, metadata, args.confidence, config, ledger
            )
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
