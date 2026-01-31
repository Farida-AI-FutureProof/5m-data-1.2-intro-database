#!/usr/bin/env python3
"""
Sanity checker for Assignment 1.2 (DBML ERD)

This script checks that:
1) assignment.md exists
2) It contains TWO dbml code blocks
3) Each block contains expected tables
"""

from __future__ import annotations

from pathlib import Path
import re


REPO_DIR = Path(__file__).resolve().parent
ASSIGNMENT_MD = REPO_DIR / "assignment.md"


def extract_dbml_blocks(md_text: str) -> list[str]:
    # Capture ```dbml ... ``` blocks (case-insensitive, allow whitespace)
    pattern = re.compile(r"```dbml\s*(.*?)\s*```", re.IGNORECASE | re.DOTALL)
    return [m.group(1).strip() for m in pattern.finditer(md_text)]


def require_contains(block: str, required: list[str], label: str) -> None:
    missing = [item for item in required if item.lower() not in block.lower()]
    if missing:
        raise SystemExit(f"[FAIL] {label}: missing {missing}")
    print(f"[OK] {label}")


def main() -> int:
    if not ASSIGNMENT_MD.exists():
        raise SystemExit("[FAIL] assignment.md not found in this folder.")

    md_text = ASSIGNMENT_MD.read_text(encoding="utf-8")
    blocks = extract_dbml_blocks(md_text)

    if len(blocks) < 2:
        raise SystemExit(f"[FAIL] Expected at least 2 dbml code blocks, found {len(blocks)}.")

    # Check Q1 block basics
    q1 = blocks[0]
    require_contains(q1, ["Table users", "Table posts", "Table follows"], "Q1 tables present")
    require_contains(q1, ["Ref:"], "Q1 has relationships (Ref)")

    # Check Q2 block basics
    q2 = blocks[1]
    require_contains(q2, ["Table customers", "Table books", "Table carts", "Table cart_items"], "Q2 tables present")
    require_contains(q2, ["Ref:"], "Q2 has relationships (Ref)")

    print("\n✅ All checks passed. You can commit + push.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
