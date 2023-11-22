#lesson 10 - section 28 - regex sub()

import re
namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Alice gave the secret documents to Agent Smith')

#this will be a find and replace. use the sub method or substitute. this will replace names with 'REDACTED'

namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Smith')

#this will replace names with partial information. in this case agent a or agent s. one word char, followed by 0 or more char


namesRegex = re.compile(r'Agent (\w)\w*')

namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Smith')

