#!/bin/bash

# Check if a directory path is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Loop through each subdirectory
for dir in "$1"/*/; do
  if [ -d "$dir" ]; then
    echo "Processing directory: $dir"
    
    # Change to the subdirectory
    cd "$dir" || continue

    # Loop through each album
    for alb in "$dir"/*/; do
        echo "Processing Album: $alb"
    done


    # Go back to the original directory
    cd - > /dev/null
  fi
done