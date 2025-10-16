# 1. import os module and print current working directory and login name
# import os
# import inspect
# print('Current working directory is:', os.getcwd())
# print('Login Name: ',os.gtelogin())
# functions = inspect.getmembers(os, inspect.isbuiltin)

# print('ALL function in os module')
# for n, function in functions:
#     print(n, end='\t')

# 2.create a folder inside current directory using python

# import os 
# cdir=os.getcwd()
# folder_name=input("Enter folder name: \t")
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print("Folder already exists")
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f"Folder {folder_name} created successfully at {folder_path}")


# 3.rename a folder
#write code to rename the folder
#u will take folder name from user
#check if folder exists, if exists rename it
import os
cdrive=os.getcwd()
oldName=input("Enter old folder name: \t")
oldFolderPath=os.path.join(cdrive,oldName)
newName=input("Enter new folder name: \t")
newFolderPath=os.path.join(cdrive,newName)
if(os.path.exists(oldFolderPath)):
    os.rename(oldFolderPath,newFolderPath)
    print(f"Folder renamed successfully to {newName}")
else:
    print("Folder does not exists")