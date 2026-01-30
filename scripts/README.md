# Utility Scripts

This directory contains scripts used to maintain and format the SDET Interview Preparation Kit.

## Scripts Overview

### 1. `reformat_questions.py`
- **Purpose**: Automatically formats the "Original Questions" section in company Markdown files.
- **Action**: 
  - Converts plain text questions into a bulleted list.
  - Splits lines that contain multiple questions (detects `?` followed by a capital letter).
  - Preserves existing headers and lists.

### 2. `convert_list_to_table.py`
- **Purpose**: Converts a simple Markdown list of companies into a numbered table.
- **Action**:
  - Adds an **ID** column with auto-incrementing numbers.
  - Adds a **Status** column with clickable checkboxes (uses `[ ]` and `[x]`).
  - Perfect for the module `_index.md` files.

### 3. `clean_headers.sh`
- **Purpose**: Batch removes unwanted text from section headers.
- **Action**:
  - Removes `(UNTOUCHED)` and `(No-BS...)` strings from all `.md` files in the company questions directory.

## How to Run

For Python scripts:
```bash
python3 scripts/reformat_questions.py
```

For Bash scripts:
```bash
chmod +x scripts/clean_headers.sh
./scripts/clean_headers.sh
```
