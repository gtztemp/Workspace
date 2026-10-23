import os

# Prompt user to enter the name of the text file
duplicates_file = input("Enter the name of the text file with duplicate file names: ").strip()

# Check if file exists
if not os.path.isfile(duplicates_file):
    print(f"File '{duplicates_file}' not found.")
    exit(1)

# Load file names to delete
with open(duplicates_file, 'r', encoding='utf-8') as f:
    files_to_delete = set(line.strip() for line in f if line.strip())

# Get current directory (folder1)
folder_path = os.getcwd()

# Delete files that match the names in the list
deleted = 0
for file in os.listdir(folder_path):
    if file in files_to_delete:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted += 1
            print(f"Deleted: {file}")

print(f"\nDone. Deleted {deleted} file(s).")

