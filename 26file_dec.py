import os

path= "C:\\Users\\NTC\\Desktop\\folder"

if os.path.exists(path):
    print("existing")
    if os.path.isfile(path):
        print("file")
    elif os.path.isdir(path):
        print("directory")
else:
    print("not existing")