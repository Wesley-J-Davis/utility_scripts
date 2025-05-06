# bash

# Define multiple lists
directories=("dir1" "dir2" "dir3")
subdirs=("subdirA" "subdirB")
filenames=("file1.txt" "file2.txt")

# Search for the file by constructing paths
for dir in "${directories[@]}"; do
    for subdir in "${subdirs[@]}"; do
        for file in "${filenames[@]}"; do
            filepath="/path/to/search/$dir/$subdir/$file"
            if [[ -f "$filepath" ]]; then
                echo "Found: $filepath"
            fi
        done
    done
done
# python
import os

# Define multiple lists
directories = ["dir1", "dir2", "dir3"]
subdirs = ["subdirA", "subdirB"]
filenames = ["file1.txt", "file2.txt"]

# Base search path
base_path = "/path/to/search"

# Construct and search for file paths
for directory in directories:
    for subdir in subdirs:
        for filename in filenames:
            filepath = os.path.join(base_path, directory, subdir, filename)
            if os.path.exists(filepath):
                print(f"Found: {filepath}")
