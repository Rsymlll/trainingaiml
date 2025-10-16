# import os 
# file_path = r'C:\AIML\Day-8\ourfiles\sample.txt'
# file=open(file_path,'w')
# content=input("Enter text to write in file: ")
# file.write(content)
# file.close()

import os
filepath = r'C:\AIML\Day-8\ourfiles'
filename=input("Enter filename to create: ")
fullpath=os.path.join(filepath,filename)
file=open(fullpath,'w')
content=input("Enter text to write in file: ")
file.write(content)
print(f'File {filename} created successfully at {fullpath}')
file.close()