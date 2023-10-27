message = 'it was a bright cold day in april, and the clocks were striking thirteen.'
count = {} 

#for loop. the setdefault starts the count at 0. update the count of the character to equal the current number + 1

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

#if yo uhave a large amount of text like in the example of the romeo and juliet story. the dictionary count will be messy.
#you can use the pprint module or pretty print.
#import pprint and then change the print command to call the modules function - pprint.pprint(count)