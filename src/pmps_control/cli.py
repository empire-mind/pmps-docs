import argparse
import json
from pathlib import Path
import yaml

from .ledger import Ledger
from .runtime import intake

def main() -> None:
    parser = argparse.ArgumentParser(prog="pmps-control")
    parser.add_argument("--config", type=Path, default=Path("config/runtime.yaml"))
    parser.add_argument("--ledger", type=Path, default=Path("data/control-ledger.sqlite3"))
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("intake")
    add.add_argument("source", type=Path)
    add.add_argument("--metadata", type=Path, required=True)
    add.add_argument("--confidence", type=float, required=True)
    replay = commands.add_parser("replay")
    replay.add_argument("record_id")
    args = parser.parse_args()
    ledger = Ledger(args.ledger)
    if args.command == "replay":
        result = ledger.replay(args.record_id)
    else:
        config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
        metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
        result = intake(args.source, metadata, args.confidence, config, ledger)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
