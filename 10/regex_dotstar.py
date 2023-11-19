#section 10 - lesson 27 - regex dot star / ^ and $

import re

beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello There!')

beginsWithHelloRegex.search('He said "Hello!"') # this wont match because hello doesnt start at the beginning of the string

# $ does the opposite of caret. just searches at the end. 

allDigitsRegex = re.compile(r'^\d+$')

allDigitsRegex.search('10928310923810923810')

allDigitsRegex.search('109283109x23810923810') #when using both ^ and $, the entire string has to match what you're looking for. in this example, it must be all digits


# . is a wildcard. any character but a new line. This example will be looking for a SINGLE character in front of at. the word flat will be 'lat'

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat the flat mat')

# .* will search any pattern, anything

'First Name: John Last Name: Wick'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: John Last Name: Wick')

#re.DOTALL will search new lines. re.IGNORECASE or re.I will ignore case