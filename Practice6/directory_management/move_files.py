import shutil
import os

os.makedirs("Backup", exist_ok=True)

# Copy file from file_handling folder
shutil.copy("../file_handling/sample.txt", "Backup/sample.txt")

# Move file
shutil.move("Backup/sample.txt", "sample_moved.txt")

# Find txt files
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)