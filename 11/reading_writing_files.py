#ch 11 - section 31 - reading and writing plaintext files


#open function
open('/Users/username/Desktop/whatever.rtf')


#this a variable to open a file, then read, and close it. 
hellofile = open('path')
hellofile.read()
hellofile.close()

#the above only allows you to read it once. you can save it to a variable to call it whenever you want.

hellofile = open('path')
content = hellofile.read()
print(content)
hellofile.close()

#this will put all the lines into multiple strings

hellofile.readlines()

#write mode will overwrite the file and create a new file. add the 'w' . it wont create new lines so add the \n command to make new lines to your text

hellofile = open('path', 'w')
hellofile.write('asdfadsfasdf')
hellofile.close()



#append mode, adds to the file

hellofile = open('path', 'a')


#shelf file. allows you to store lists and dictionaries and non text data to a file and reopen them in the future with your py program

import shelve
shelffile = shelve.open('mydata')
shelffile['names'] = ['homer', 'marge', 'bart', 'lisa', 'maggie']
shelffile.close()


shelffile = shelve.open('mydata')
shelffile.keys()

list(shelffile.keys())

list(shelffile.values())