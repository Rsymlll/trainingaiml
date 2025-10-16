import os
filepath=os.getcwd()
filename=input("Enter filename to update the file: ")
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'a')
    content=input("Enter text to add in file: ")
    file.write(content)
    print(f'File {filename} updated successfully')
    file.close()
else:
    print(f'File {filename} does not exist in {filepath}')