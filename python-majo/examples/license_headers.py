"""
license_headers: examples of license headers for Python files
  with all my heart, 2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""

# =============================================================================
# CANONICAL FORMAT
# =============================================================================
#
# This is the standard header format for all Python files:
#
#   """
#   project-name: brief description
#     with all my heart, YEAR-YEAR, mark joshwel <mark@joshwel.co>
#     SPDX-License-Identifier: Unlicense OR 0BSD
#   """
#
# Key points:
# - First line: project name and brief description
# - Second line: attribution with year range (indented 2 spaces)
# - Third line: SPDX identifier (indented 2 spaces)
# - Use year range for ongoing projects (e.g., 2024-2025)
# - Use single year for one-off scripts (e.g., 2025)


# =============================================================================
# EXAMPLE 1: Library/Project Header
# =============================================================================

LIBRARY_HEADER = '''
"""
tomlantic: marrying pydantic models and tomlkit documents
  with all my heart, 2024-2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""
'''


# =============================================================================
# EXAMPLE 2: One-off Script Header
# =============================================================================

SCRIPT_HEADER = '''
"""
cleanup: removes temporary build artefacts
  with all my heart, 2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""
'''


# =============================================================================
# EXAMPLE 3: With PEP 723 (for uv run scripts)
# =============================================================================
#
# For scripts that can be run directly with `uv run script.py`,
# add PEP 723 metadata before the docstring header.

PEP723_HEADER = '''
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "tqdm",
#     "rich",
# ]
# ///
"""
convert: batch converts files to new format
  with all my heart, 2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""

from tqdm import tqdm

def main():
    ...

if __name__ == "__main__":
    main()
'''


# =============================================================================
# SPDX LICENSE IDENTIFIERS
# =============================================================================
#
# The SPDX identifier provides machine-readable licensing information.
# Default to "Unlicense OR 0BSD" (dual-licensed) for maximum flexibility.

SPDX_EXAMPLES = {
    # For most files (dual-licensed) - DEFAULT
    "dual": "SPDX-License-Identifier: Unlicense OR 0BSD",
    # For files by contributors who cannot waive copyright
    "zero_bsd_only": "SPDX-License-Identifier: 0BSD",
    # For pure Unlicense
    "unlicense_only": "SPDX-License-Identifier: Unlicense",
}
