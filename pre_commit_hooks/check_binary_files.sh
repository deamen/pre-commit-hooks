#!/bin/bash

# Initialize an empty variable to store binary file names
binary_files=""

# Get the list of files added or modified in the commit
files=$(git diff --cached --name-only --diff-filter=AM)

if [ -z "$files" ]; then
  echo "No files detected in the commit."
  exit 1
fi

# Check each file for binary content
for file in $files; do
  if file "$file" | grep -q 'ELF\|PE32\|Mach-O'; then
    binary_files="$binary_files$file\n"
  fi
done

# Exit with error if binary files were detected
if [ -n "$binary_files" ]; then
  echo "Binary files detected:"
  echo -e "$binary_files"
  exit 1
else
  echo "No binary files detected."
fi
