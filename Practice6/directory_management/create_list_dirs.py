import os 
# Create directory
os.mkdir("TestFolder")
# Create nested directories
os.makedirs("FolderA/FolderB", exist_ok=True)
# Current working directory
print(os.getcwd())
# List files and folders
print(os.listdir())
# Remove directory
os.rmdir("TestFolder")