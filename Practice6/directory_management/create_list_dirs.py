import os

# Create directory
os.mkdir("TestFolder")

# Create nested directories
os.makedirs("FolderA/FolderB", exist_ok=True)

# Create a test file inside FolderB
with open("FolderA/FolderB/test.txt", "w") as file:
    file.write("This is a test file.")

# Current working directory
print(os.getcwd())

# List files and folders
print(os.listdir())

# Remove TestFolder
os.rmdir("TestFolder")