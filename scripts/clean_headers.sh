#!/bin/bash

# Directory containing the content
TARGET_DIR="content/12_company_based_questions"

echo "Cleaning up headers in $TARGET_DIR..."

# Remove (UNTOUCHED)
find "$TARGET_DIR" -name "*.md" -exec sed -i 's/ (UNTOUCHED)//g' {} +

# Remove (No-BS Java QA / SDET Explanations)
find "$TARGET_DIR" -name "*.md" -exec sed -i 's/ (No-BS Java QA \/ SDET Explanations)//g' {} +

echo "Done!"
