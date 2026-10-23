import os
import shutil

# Prompt user to enter the name of the text file
duplicates_file = input("Enter the name of the text file with duplicate file names: ").strip()

# Check if the text file exists
if not os.path.isfile(duplicates_file):
    print(f"File '{duplicates_file}' not found.")
    exit(1)

# Load file names from the text file
with open(duplicates_file, 'r', encoding='utf-8') as f:
    files_to_move = set(line.strip() for line in f if line.strip())

# Current working directory (folder1)
folder1_path = os.getcwd()

# Create a new folder to move duplicates into
moved_folder_name = 'duplicates_moved'
moved_folder_path = os.path.join(folder1_path, moved_folder_name)
os.makedirs(moved_folder_path, exist_ok=True)

# Move files
moved = 0
for file in os.listdir(folder1_path):
    if file in files_to_move:
        source = os.path.join(folder1_path, file)
        destination = os.path.join(moved_folder_path, file)
        if os.path.isfile(source):
            shutil.move(source, destination)
            moved += 1

print(f"\nDone. Moved {moved} file(s) to '{moved_folder_name}/'.")

