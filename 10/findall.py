#section 26 - find all in regex

import re

phoneRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')

phoneRegex.findall()

#the example uses a resume variable with a resume as a string in triple quotes e.g. '''blah blah 123-123-1234 or cell 800-812-1234'''

resume = '''Ebony Moore
Seattle, WA | 206-555-0149 | 206-555-1234 | emoore@email.com
Summary
&nbsp;
Determined Accountant with three years of experience in personal and tax accounting. Excellent skills in mathematics, communication and organization with great proficiency in various accounting software.
Education
&nbsp;
Cloverfield College
Bachelor of Business Administration in accounting
Experience
&nbsp;
Gilmore Financial, New Orleans, LA, Certified Public Accountant
Oct. 2021 – Current

    Meet with clients to discuss their accounting needs
    Compute taxes for clients during tax season
    Monitoring and recording activity for accounts payable and accounts receivable
    Prepare balance sheets for corporate clients
    Create budget forecasts for clients to help with financial planning

Harrison Money Management, New Orleans, LA, Accountant
Aug. 2020 – Oct. 2021

    Prepared tax returns for clients during tax season
    Helped the internal audit team complete annual audits
    Updated monthly reports to reflect the financial standings of each client

Harrison Money Management, New Orleans, LA, Junior Accountant
May 2019 – Aug. 2020

    Maintained accounts receivable and accounts payable for the department
    Reviewed monthly payroll to ensure it's accurate before distribution
    Prepared financial reports to share with clients

Certifications
&nbsp;

    Certified Public Accountant (CPA)
    Certified Financial Analyst (CFA)

Skills
&nbsp;

    Proficiency in accounting software
    Basic mathematics
    Organizational skills
    Attention to detail
    Communication skills'''

phoneRegex.search(resume)
#this will find only the first the number

phoneRegex.findall(resume)
#returns a list value with strings. the findall method will return strings if whatever it is searching doesnt have groups. If there are groups, it returns a list of tuples


#character class for regex
# \d - numeric digit 0-9
# \D - any character that isnt a numeric digit from 0-9
# \w - any letter, numeric digit, pr underscore
# \W - any character that is not a letter, numeric digit, or underscore
# \s - any space, tab, or newline character
# \S - any character that is not a space, tab, or newline


lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling bir ds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+') #d for digit, + for more than one digit. s for space. w for word, + for more than one word
xmasRegex.findall()

vowelRegex = re.compile(r'[aeiouAEIOU]') # same as (r'(a|e|i|o|u))
vowelRegex.search('some random string')

#you can put a ^ in front and it will find everything that isnt a vowel or whatever in your raw string, including punctuation
#e.g. (r'[^aeiouAEIOU]')
