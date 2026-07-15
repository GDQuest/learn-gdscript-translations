#!/usr/bin/env python3
"""Normalize PO formatting or remove obsolete entries with polib."""

import argparse
from pathlib import Path

import polib


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="A .po file or directory containing .po files")
    parser.add_argument("--dry-run", action="store_true", help="List files that would be rewritten")
    parser.add_argument("--remove-obsolete", action="store_true", help="Remove #~ obsolete entries instead of only normalizing")
    args = parser.parse_args()

    if args.path.is_file() and args.path.suffix == ".po":
        files = [args.path]
    elif args.path.is_dir():
        files = sorted(args.path.rglob("*.po"))
    else:
        parser.error("path must be a .po file or directory")

    for path in files:
        po = polib.pofile(str(path))
        obsolete_count = len(po.obsolete_entries())
        if args.dry_run:
            suffix = f": {obsolete_count} obsolete entries" if args.remove_obsolete else ""
            print(f"{path}{suffix}")
            continue
        if args.remove_obsolete:
            if not obsolete_count:
                continue
            po[:] = [entry for entry in po if not entry.obsolete]
        po.save(str(path))
        suffix = f": removed {obsolete_count} obsolete entries" if args.remove_obsolete else ""
        print(f"{path}{suffix}")


if __name__ == "__main__":
    main()
