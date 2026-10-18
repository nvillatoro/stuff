#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")


def extract_imports(path: Path) -> list[dict[str, str]]:
    imports = []
    text = path.read_text(encoding="utf-8")

    for match in LINK_RE.finditer(text):
        label, target = match.groups()
        target = target.strip()

        if not target or target.startswith("#"):
            continue
        if "://" in target:
            continue

        normalized = target.split("#", 1)[0]
        if not normalized.lower().endswith(".md"):
            continue

        resolved = (path.parent / normalized).resolve()
        imports.append(
            {
                "label": label,
                "target": target,
                "resolved": str(resolved),
                "exists": resolved.exists(),
            }
        )

    return imports


def build_graph(entry: Path) -> tuple[dict[str, dict], list[str]]:
    graph: dict[str, dict] = {}
    missing: list[str] = []
    stack = [entry.resolve()]
    seen: set[Path] = set()

    while stack:
        current = stack.pop()
        if current in seen:
            continue

        seen.add(current)

        if not current.exists():
            missing.append(str(current))
            continue

        imports = extract_imports(current)
        graph[str(current)] = {"imports": imports}

        for item in imports:
            target = Path(item["resolved"])
            if item["exists"] and target not in seen:
                stack.append(target)
            elif not item["exists"]:
                missing.append(item["resolved"])

    return graph, sorted(set(missing))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve local Markdown prompt imports for analysis."
    )
    parser.add_argument("entry_file", help="Entry Markdown prompt file")
    args = parser.parse_args()

    entry = Path(args.entry_file).expanduser()
    if not entry.exists():
        print(json.dumps({"error": f"entry file not found: {entry}"}))
        return 1

    graph, missing = build_graph(entry)
    print(
        json.dumps(
            {
                "entry_file": str(entry.resolve()),
                "graph": graph,
                "missing": missing,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
