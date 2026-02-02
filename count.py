#!/usr/bin/env python3
"""
count.py — analyse skill sizes and update README.md

  with all my heart, 2024-2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""

import os
import re
from pathlib import Path


def analyse_skills(skills_dir: Path) -> list[dict]:
    """analyse all skills in the given directory."""
    results = []

    for skill_name in sorted(os.listdir(skills_dir)):
        skill_path = skills_dir / skill_name
        if skill_path.is_dir():
            skill_md = skill_path / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding="utf-8")
                lines = len(content.split("\n"))
                words = len(content.split())

                if lines <= 500:
                    status = "OK"
                elif lines <= 800:
                    status = "WARNING"
                else:
                    status = "TOO LONG"

                results.append(
                    {
                        "name": skill_name,
                        "lines": lines,
                        "words": words,
                        "status": status,
                    }
                )

    return results


def generate_table(results: list[dict]) -> str:
    """generate markdown table of results."""
    lines = ["| skill | lines | words | status |", "|-------|-------|-------|--------|"]

    for r in results:
        status_emoji = (
            "🟢" if r["status"] == "OK" else "🟡" if r["status"] == "WARNING" else "🔴"
        )
        lines.append(
            f"| `{r['name']}` | {r['lines']} | {r['words']} | {status_emoji} |"
        )

    return "\n".join(lines)


def update_readme(readme_path: Path, table: str) -> bool:
    """update README.md with the new table."""
    content = readme_path.read_text(encoding="utf-8")

    # find and replace the skills size table section
    # match from "## skill sizes" until the next "## " (next section)
    pattern = r"(## skill sizes\n\n)(.*?)(\n## )"
    replacement = f"\1{table}\n\nrun `count.py` to update this table.\3"

    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        readme_path.write_text(new_content, encoding="utf-8")
        return True
    else:
        # table section doesn't exist - look for the sizes subsection
        sizes_pattern = r"(### sizes\n\n)(.*?)(\n## )"
        if re.search(sizes_pattern, content, re.DOTALL):
            new_content = re.sub(
                sizes_pattern,
                f"\1trying not to overbloat the skills as per [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)\n\n{table}\n\nrun `count.py` to update this table.\3",
                content,
                flags=re.DOTALL,
            )
            readme_path.write_text(new_content, encoding="utf-8")
            return True
        return False


def main() -> int:
    """main entry point."""
    skills_dir = Path(__file__).parent
    readme_path = skills_dir / "README.md"

    print("analysing skills...")
    print()

    results = analyse_skills(skills_dir)

    # print to console
    for r in results:
        print(
            f"{r['name']:35s} {r['lines']:4d} lines  {r['words']:5d} words  [{r['status']}]"
        )

    print()

    # generate and update readme
    table = generate_table(results)

    if readme_path.exists():
        update_readme(readme_path, table)
        print(f"updated {readme_path}")
    else:
        print(f"warning: {readme_path} not found, skipping update")

    # check for issues
    warnings = [r for r in results if r["status"] == "WARNING"]
    too_long = [r for r in results if r["status"] == "TOO LONG"]

    if too_long:
        print(
            f"\nerror: {len(too_long)} skill(s) exceed 800 lines and need immediate attention:"
        )
        for r in too_long:
            print(f"  - {r['name']}: {r['lines']} lines")
        return 1

    if warnings:
        print(f"\nwarning: {len(warnings)} skill(s) exceed 500 lines (optimal target):")
        for r in warnings:
            print(f"  - {r['name']}: {r['lines']} lines")
        return 0

    print("\nall skills are within the 500-line optimal target ✓")
    return 0


if __name__ == "__main__":
    exit(main())
