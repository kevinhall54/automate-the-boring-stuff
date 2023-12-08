#chapter 11 - section 30 - files

import os

#get the file path in the os youre working in
os.path.join('folder1', 'folder2', 'file.png')

#get current working directory
os.getcwd()

#change dir - os.chdir(/folder/folder1/file.png)
os.chdir()

#. is for the folder youre in. if there was another folder in your cwd, it would be ./folder2. .. is the root folder. 

#gives you the absolute path
os.path.abspath() 

#t/f if its an absolute path
os.path.isabs()

#gives you the relative path from some starting point
os.path.relpath()

#gives you the filename in the path - file.png
os.path.basename()

#checks if its a file
os.path.isfile()

#gives you file size
os.path.getsize()

#list dir
os.listdir()

#get total size in bytes of files in the a folder
totalsize = 0
for filename in os.listdir('path'):
    if os.path.isfile(os.path.join('path', filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('path', filename))


#make dir put in a relative or abs path
os.makedirs()