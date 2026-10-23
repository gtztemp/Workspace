import os

# Use the current working directory (where the script is executed)
directory_path = os.getcwd()

# Name of the output text file
output_file = 'directory_contents.txt'

# Get the script filename
script_file = os.path.basename(__file__)

# Get list of all items in the directory
items = os.listdir(directory_path)

# Filter out the script file
items = [item for item in items if item != script_file]

# Filter for folders and files, then combine them
folders = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]
files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
all_items = folders + files  # Combine folders and files into one list

# Write numbered list of folder and file names to a text file in the same directory
with open(os.path.join(directory_path, output_file), 'w') as f:
    for index, item in enumerate(all_items, start=1):
        f.write(f"{index}- {item}\n")

print(f"Folder and file names have been saved to {output_file}")
