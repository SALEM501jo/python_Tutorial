import os

file_name="D:\\vscode\\copy2.txt"
new_place="D:\\new_place\\copy.txt"
try:
    if os.path.exists(new_place):
        print("file name already exists")
    else:
        os.replace(file_name,new_place)
        print("file is moved")
except FileNotFoundError:
    print("File not found")
except Exception:
    print("Could not replace something went wrong :(  ")
