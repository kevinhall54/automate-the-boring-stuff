#ch 11 - section 33 - deleting files. almost all of these will permanently delete

import os
os.unlink('filename') #relative path or exact path


os.getcwd() #reminder for current working dir

os.rmdir('dir path') #folder has to be empty


#delete entire dir and contents
import shutil
shutil.rmtree('dir')



#dry run - typo in extension is following the example. print function is to check to make sure youre deleting the correct file

import os

os.chdir('dir')

for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)


#use the send2trash module - needs to be installed via pip

import send2trash
send2trash.send2trash('file')
