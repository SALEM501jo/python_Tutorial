import os 
import shutil
file_name="salem.txt"
fol_name="folder"
try:
   if os.path.exists(fol_name):
      print("the folder exists")
      #os.remove(file_name)#* for files 
      #os.rmdir(fol_name) #* for empty folders
      #shutil.rmtree(fol_name)#* for folders that contain files its considered a dangerous function  
except FileNotFoundError:
   print("the file does not exist")
except PermissionError:
   print("u dont have permission to delete this folder")
except OSError:
   print("u can't delete that using this function")
except Exception:
   print("something went wrong")
else:
   print(fol_name +" is removed")