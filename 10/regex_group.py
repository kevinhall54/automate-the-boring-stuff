#s10,e24 - regex groups and | 

#

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#this will return a match object and you want to store that in a group or variable
phoneNumRegex.search('My number is 555-555-5555')

mo = phoneNumRegex.search('My number is 555-555-5555')
mo.group() # this will return just the number


#if you put () around the characters you want returned, it will create groups. in this case, area code, first 3, last 4.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#run a search again and then put it in a group
phoneNumRegex.search('My number is 555-555-5555')
mo = phoneNumRegex.search('My number is 555-555-5555')

#then you can search by group with the integer 1 or 2
mo.group(1)

# | will match one of several patterns of your regex. the following will match whatever is in the raw string

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()