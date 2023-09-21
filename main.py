# read list of directories from file
import os.path

with open('directories.txt') as f:
    directories = f.read().splitlines()
print("Directories to wipe:")
print(*directories, sep='\n')

# read list of files to keep from file
with open('keep_files.txt') as f:
    keep_files = f.read().splitlines()
print("Files to keep:")
print(*keep_files, sep='\n')

# loop through directories
for dir1 in directories:
    # delete files not in keep list
    with os.scandir(dir1) as files:
        for file in files:
            if file.is_file():
                filename = file.name
                if filename not in keep_files:
                    os.remove(os.path.join(dir1, filename))
                    print("Removed file: ", filename)
                else:
                    print("Kept file: ", filename)
            else:
                print(f"Did not remove {file}, not a file")
print("Done")
