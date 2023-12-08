#ch 11 - section 32 - moving files and folders

import shutil

shutil.copy('sourcefilepath', 'destinationpath')

#you can rename it at the same time.

shutil.copy('sourcefilepath', 'destination/sadfasdf.txt')

shutil.copytree('sourcefolder', 'destinationfolder') 

shutil.move('source', 'destination')


