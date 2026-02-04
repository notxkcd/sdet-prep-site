#!/bin/bash
FOLDER="${1:-.}"
for file in "$FOLDER"/*.md; do
  if [ ! -f "$file" ]; then continue; fi
  if grep -q "^category:" "$file"; then
    echo "Skipping $file (category exists)"
    continue
  fi
  sed -i '/^---/!b;n;/^---/b;i\
category: "Java"
' "$file"
  echo "Added to $file"
done
