#Lists - lists are a value with multiple values. They are in brackets and are comma separated - ['cat', 'bat']
# call the item in the list by calling the variable and then the number in brackets 

#spam = ['cat', 'bat', 'something']
#spam[0] - will be cat


#for loops with lists
#code in the lesson

#for loop

for i in range(4):
    print(i)

list(range(4))
#this should return a list of [0, 1, 2, 3]

list(range(0, 100, 2))
#this will return the numbers from 0 to 100 in increments of 2


#for loop with index and list value
supplies = ['pens', 'staplers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])



cat = ['medium', 'spotted', 'extra loud']
#instead of multuple variables, e.g. size = cat[0] or color = cat[1], you can have multiple assignments on the variables on the left side of the operator

size, color, disposition = cat

#can have multiple variables on right side as well

size, color, disposition = 'fat', 'spotted', 'loud'


#variable swapping

a = 'AAA'
b = 'BBB'

#can swap by doing this

a, b = b, a

#augmented assignment operators

spam = 42
spam = spam + 1 #to increment by 1

#you can just do this

spam += 1

#end of lesson recap/notes
#for loops technically iterate over the values in a list
#range() function returns a list like value, which can be passed to the list() function if you need an actual list value
#you can swap varaibles using multiple assignments
#augmented assignments are shortcuts for +-*/ and %

#list methods
# index(), append(), insert(), remove(), sort()

#same as a function but called/attached on a certain value


spam = ['hello', 'hi', 'howdy']
spam.index('hello')

#this should called 0

#append adds to end of list
spam.append('konnichiwa')

#insert adds it where you want it. The following will add it to index spot 1

spam.insert(1, 'yaho')

#append and insert can only be used on lists, not strings or integers

#remove is self explanatory but you can use it to remove an item from an index

spam.remove('hi')

#you can also use delete to delete a certain intem from the list.

del spam[0]



