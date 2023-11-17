#lesson 25 - repetition in regex and matching

import re   

# This is a way to match words, but you can do it like the example below not commented out
# batRegex = re.compile(r'Batman|Batwoman')

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
mo.group()

#this requires the area code and will only match if the area code is in the string
phoneRegex = re.copmpile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.search('My phone number is 858-555-5123, call me tomorrow')
mo.group()

#this will make the area code optional by adding it into a separate group
phoneRegex = re.copmpile(r'(\d\d\d)-\d\d\d-\d\d\d\d')

#* = match 0 or more times in regex. called star instead of asterisk
batRegex = re.compile(r'Bat(wo)*man')

#+ is match 1 or more times
batRegex = re.compile(r'Bat(wo)+man')
batRegex.search('The adventures of Batman') #this will not return anything since wo is not in this.

