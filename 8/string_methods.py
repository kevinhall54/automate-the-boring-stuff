#string methods - lesson 20
#string methods return a new string rather than update


spam = 'Hello World'
spam.upper()
# this will return hello world in caps
spam.lower()
# does the opposite of upper


#isalpha, isalnum, isdecimal, isspace, istitle, startswith, endswith

#join - useful when you need to join strings together into a single string value

','.join(['cats', 'rats', 'bats'])

#this will put a comma in between them all and give you an output of 'cats,rats,bats'
#if just '' or ' ', this will put no spaces or put a space respectively

