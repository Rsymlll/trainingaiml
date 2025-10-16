import os
filepath=os.getcwd()
filename=input("Enter filename to update the file: ")
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'r')
    content=file.read()
    print(f'File content as follows')
    print.close()
    file.close()
else:
    print(f'File {filename} does not exist in {filepath}')