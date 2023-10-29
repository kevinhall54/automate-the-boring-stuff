#advanced string syntax

#write print or access strings in code

'Hello'
'That is Alice's cat' 
#this creates an error because of the the extra apostrophe. You can fix this with the below syntax

"That is Alice's cat"

#escape characters, \ before the character. e.g. Alice\'s cat
#other examples 
# \"  for double quote
# \t for tab 
# \n for new line or line break
# \\ for backslash

#example below

print('Hello there!\nHow are you?\nI\'m fine')


#raw string - same as normal string but begins with lower case r before. helpful for regex or code with a lot of backslashes
r'Hello'
r'That is Alice\'s cat'

#you can have a multiline strings with triple quotes """" or '''. 

print("""something something
      more stuff
      and additional stuff
      hi 
      hi
      nani?""")

#indexes slices and the in and not in operators all work with strings

spam = "hello world"

spam[0]
spam[1:5]
spam[-1]
'Hello' in spam
'HELLO' in spam
