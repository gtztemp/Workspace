import os
import shutil

# Prompt user to enter the name of the text file
whitelist_file = input("Enter the name of the text file with file names to KEEP: ").strip()

# Check if the text file exists
if not os.path.isfile(whitelist_file):
    print(f"File '{whitelist_file}' not found.")
    exit(1)

# Load file names from the text file (files to keep)
with open(whitelist_file, 'r', encoding='utf-8') as f:
    files_to_keep = set(line.strip() for line in f if line.strip())

# Current working directory (folder1)
folder1_path = os.getcwd()

# Create a new folder to move the other files into
moved_folder_name = 'moved'
moved_folder_path = os.path.join(folder1_path, moved_folder_name)
os.makedirs(moved_folder_path, exist_ok=True)

# Move files not in the whitelist
moved = 0
for file in os.listdir(folder1_path):
    source = os.path.join(folder1_path, file)
    if os.path.isfile(source) and file not in files_to_keep and file != os.path.basename(__file__):
        destination = os.path.join(moved_folder_path, file)
        shutil.move(source, destination)
        moved += 1

print(f"\nDone. Moved {moved} file(s) not listed in '{whitelist_file}' to '{moved_folder_name}/'.")

