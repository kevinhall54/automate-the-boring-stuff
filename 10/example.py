#regex basics - notes and examples

#non regex to recognize phone number


""" def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number sized
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing data
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

print(isPhoneNumber('123-456-7890'))

#to find a phone number in a string

message = 'call me at 123-456-1234 tomorrow, or 123-456-7812 the day after'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found:' + chunk)
        foundNumber = True
if not foundNumber:
    print("could not find any phone numbers")


#regex
 """

#this will find the first instance of a phone number. \d is the regex syntax for finding a digit. you need the r for raw string. you will need to import the
#re module

import re

message = 'call me at 123-456-1234 tomorrow, or 123-456-7812 the day after'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

# the same as above but with findall 

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('call me at 123-456-1234 tomorrow, or 123-456-7812 the day after'))
