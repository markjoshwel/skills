---
name: public-domain-setup-majo
description: Set up public domain repositories with dual licensing (Unlicense OR 0BSD). Use when initializing a new repository or converting an existing one to public domain. Fetches authoritative license files and configures the repository according to Mark's standards.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
  default_author: Mark Joshwel
  default_email: mark@joshwel.co
---

# Public Domain Repository Setup (Mark)

Automated setup for public domain repositories with dual licensing (Unlicense OR 0BSD).

## Overview

This skill sets up repositories to be free-as-in-freedom, dual-licensed under The Unlicense or the BSD Zero Clause License (SPDX: `Unlicense OR 0BSD`).

**The Spirit**: Treat the work as public domain via The Unlicense, but provide the BSD Zero Clause License where public domain dedication is not possible due to policies bound to a contributor or their employer.

## When to Use This Skill

- Initializing a new repository
- Converting an existing repository to public domain
- Setting up licensing for a new project
- Ensuring consistent public domain structure

## Prerequisites

- Git repository (initialized or not)
- Internet access to fetch authoritative files
- Default author: Mark Joshwel <mark@joshwel.co>

## Setup Workflow

### Step 1: Check Repository State

Determine if this is a new repository or existing:

```bash
# Check if git repo exists
if [ -d .git ]; then
    echo "Existing repository"
else
    echo "New repository - will initialize"
fi

# Check for existing license files
ls -la LICENSE* 2>/dev/null || echo "No LICENSE files found"
ls -la UNLICENSE* 2>/dev/null || echo "No UNLICENSE file found"
```

### Step 2: Handle Existing Files (CRITICAL)

**If LICENSE, COPYING, or similar files exist:**

STOP and ask the user:

```
I found existing license files in this repository:
- [List existing files]

How would you like to proceed?
1. Replace with public domain dual-license setup
2. Keep existing licenses and add public domain as additional option
3. Abort setup
4. Something else (describe)
```

**Do not proceed without user guidance when clashes exist.**

### Step 3: Fetch Authoritative Files

Fetch all files from authoritative sources:

```bash
# Create temporary directory for downloads
mkdir -p /tmp/pd-setup

# Fetch all files
curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/CODE_OF_CONDUCT.md -o /tmp/pd-setup/CODE_OF_CONDUCT.md

curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/CONTRIBUTING -o /tmp/pd-setup/CONTRIBUTING

curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/LICENCING -o /tmp/pd-setup/LICENCING

curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/LICENSE-0BSD -o /tmp/pd-setup/LICENSE-0BSD

curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/UNLICENSE -o /tmp/pd-setup/UNLICENSE
```

### Step 4: Update Copyright Year

**CRITICAL**: Update the copyright year in LICENSE-0BSD to the current year:

```bash
# Get current year
CURRENT_YEAR=$(date +%Y)

# Update LICENSE-0BSD with current year
sed -i "s/Copyright (C) [0-9]\{4\}/Copyright (C) $CURRENT_YEAR/" /tmp/pd-setup/LICENSE-0BSD

# Verify the change
grep "Copyright" /tmp/pd-setup/LICENSE-0BSD
```

**Note**: Due to British English conventions, the file is named "LICENCING" (with 'c'), but LICENSE-0BSD and UNLICENSE use American spelling "LICENSE" (with 's') for standards compatibility.

### Step 5: Place Files

Copy files to repository root:

```bash
# Copy all files to repository root
cp /tmp/pd-setup/CODE_OF_CONDUCT.md ./CODE_OF_CONDUCT.md
cp /tmp/pd-setup/CONTRIBUTING ./CONTRIBUTING
cp /tmp/pd-setup/LICENCING ./LICENCING
cp /tmp/pd-setup/LICENSE-0BSD ./LICENSE-0BSD
cp /tmp/pd-setup/UNLICENSE ./UNLICENSE

# Clean up
rm -rf /tmp/pd-setup
```

### Step 6: Initialize Git (if needed)

**IMPORTANT**: Initialize git repository if it doesn't exist:

```bash
# Initialize git if not already initialized
if [ ! -d .git ]; then
    git init
    echo "Git repository initialized"
fi
```

This skill is designed to be called at the opportune time to set up a repository, so initializing git is appropriate.

### Step 7: Verify Setup

Check that all files are in place:

```bash
# List all public domain files
echo "=== Public Domain Repository Files ==="
ls -la CODE_OF_CONDUCT.md CONTRIBUTING LICENCING LICENSE-0BSD UNLICENSE 2>/dev/null

echo ""
echo "=== LICENSE-0BSD Copyright Year ==="
head -1 LICENSE-0BSD

echo ""
echo "=== LICENCING Content Preview ==="
head -10 LICENCING
```

## File Descriptions

| File | Purpose | Source |
|------|---------|--------|
| `CODE_OF_CONDUCT.md` | Community conduct guidelines | Fetched from gist |
| `CONTRIBUTING` | Contribution guidelines with waiver | Fetched from gist |
| `LICENCING` | Dual-licensing explanation (British spelling) | Fetched from gist |
| `LICENSE-0BSD` | BSD Zero Clause License text | Fetched from gist |
| `UNLICENSE` | Public domain dedication | Fetched from gist |

## SPDX License Identifiers

When creating new source files, add the appropriate SPDX identifier at the top:

**For most files** (dual-licensed):
```python
# SPDX-License-Identifier: Unlicense OR 0BSD
```

**For files by contributors who cannot waive copyright**:
```python
# SPDX-License-Identifier: 0BSD
```

**Note**: SPDX identifiers in source files are covered by the `majo-standards` skill. This skill focuses on repository-level setup.

## Complete Setup Script

Here's the complete workflow in one go:

```bash
#!/bin/bash
# Public Domain Repository Setup

set -e

echo "=== Public Domain Repository Setup ==="
echo ""

# Check for existing license files
EXISTING=$(ls LICENSE* COPYING* 2>/dev/null || true)
if [ -n "$EXISTING" ]; then
    echo "WARNING: Existing license files found:"
    echo "$EXISTING"
    echo ""
    echo "Please resolve conflicts before proceeding."
    exit 1
fi

# Create temp directory
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

# Fetch files
echo "Fetching authoritative files..."
curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/CODE_OF_CONDUCT.md -o "$TMPDIR/CODE_OF_CONDUCT.md"
curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/CONTRIBUTING -o "$TMPDIR/CONTRIBUTING"
curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/LICENCING -o "$TMPDIR/LICENCING"
curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/LICENSE-0BSD -o "$TMPDIR/LICENSE-0BSD"
curl -sL https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/9cd9bd30475b761823cf6e8920fba268766f3408/UNLICENSE -o "$TMPDIR/UNLICENSE"

# Update copyright year
CURRENT_YEAR=$(date +%Y)
sed -i "s/Copyright (C) [0-9]\{4\}/Copyright (C) $CURRENT_YEAR/" "$TMPDIR/LICENSE-0BSD"

# Copy files
echo "Installing files..."
cp "$TMPDIR"/* .

# Initialize git if needed
if [ ! -d .git ]; then
    git init
    echo "Git repository initialized"
fi

echo ""
echo "=== Setup Complete ==="
echo "Files installed:"
ls -la CODE_OF_CONDUCT.md CONTRIBUTING LICENCING LICENSE-0BSD UNLICENSE
echo ""
echo "Copyright year: $CURRENT_YEAR"
```

## Post-Setup Steps

After running this skill:

1. **Review files** - Ensure they meet your project's needs
2. **Add to git**:
   ```bash
   git add CODE_OF_CONDUCT.md CONTRIBUTING LICENCING LICENSE-0BSD UNLICENSE
   git commit -m "Add public domain dual-licensing"
   ```
3. **Update AGENTS.md** - Note the licensing choice
4. **Add SPDX identifiers** to source files (see `majo-standards` skill)

## Common Issues

### Issue: curl fails to fetch

**Solution**: Check internet connection and gist URLs. The URLs should be:
- `https://gist.githubusercontent.com/markjoshwel/6a0b4ea7673c279bc5a2fb5fe4ed423e/raw/...`

### Issue: sed not working on macOS

**Solution**: Use `sed -i ''` instead of `sed -i` on macOS:
```bash
sed -i '' "s/Copyright (C) [0-9]\{4\}/Copyright (C) $CURRENT_YEAR/" LICENSE-0BSD
```

### Issue: Existing LICENSE file

**Solution**: This skill will stop and ask for guidance. Do not overwrite without user confirmation.

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance
- Universal code principles
- Documentation policies

Works alongside:
- `python-majo` / `js-bun-majo` / `shell-majo` — For language-specific project setup
- `task-planning-majo` — For complex repository setups
- `git-majo` — For committing license files
- `docs-majo` — For writing licence documentation

## References

- [The Unlicense](https://unlicense.org/)
- [BSD Zero Clause License](https://opensource.org/licenses/0BSD)
- [SPDX License List](https://spdx.org/licenses/)

## Notes

- **British vs American spelling**: LICENCING uses British spelling (with 'c'), while LICENSE-0BSD and UNLICENSE use American spelling (with 's') for compatibility with standards
- **Copyright year**: Always updated to current year automatically
- **Author**: Defaults to Mark Joshwel <mark@joshwel.co>
