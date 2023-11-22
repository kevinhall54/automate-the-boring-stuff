# lesson 10 - section 29 - regex program - phone/email scraper

#!python

import pyperclip, re

phoneRegex = re.compile(r'''(
    ((\d\d\d) | (\(\d\d\d\)))? # area code (optional) - (\d\d\d\) | (\(\d\d\d\)))? | 
    (\s|-) # first separator - (\s | -)
    \d\d\d  # first 3 digits \d\d\d 
    - # separator - -
    \d\d\d\d # last 4 digits - \d\d\d\d
    (((ext(\.)?\s)|x) # extension (optional word/letter) - (((ext(\.)?\s)|x) 
    (\d{2-5}))? # extension (optional number) - (\d{2-5}))?
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9_.+]+ # name - [a-zA-Z0-9_.+]+
    @               # @ symbol - @
    [a-zA-Z0-9_.+]+ # domain name - [a-zA-Z0-9_.+]+ 
)''', re.VERBOSE)

# To Do list:
# Create Regex for phone numbers - patterns - 858-555-1234, 555-1234, (858) 555-1234, 555-1234 ext 12345, ext. 12345, x12345
   
# Create Regex for email address
    # name - [a-zA-Z0-9_.+]+
    # @ symbol - @
    # domain name - [a-zA-Z0-9_.+]+

# get text off clipboard
text = pyperclip.paste()

# extract email/phone from text
phoneRegex.findall(text)

# copy extracted email/phone to clip
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#the output for numbers will be a list of tuples. this will get index 0 of each list and separate it out
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
