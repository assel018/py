# Create a file and write data 
with open("sample.txt", "w") as file: 
    file.write("Hello World\n") 
    file.write("Python File Handling\n") 
# Append new data 
with open("sample.txt", "a") as file: 
    file.write("This line was appended.\n") 
print("Data written successfully.")
