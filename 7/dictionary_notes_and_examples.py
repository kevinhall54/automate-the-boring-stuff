#section 7 - dictionaries

#dictionaries are in curly brackets and inside contain key value pairs

myCat = {'size': 'fat', 'color': 'spotted', 'disposition': 'loud'}

#you can access the values through the keys

myCat[size] #this will give you the value of whatever in the key size

'my cat has ' + myCat['color'] + ' fur'

# you can list out the keys or the values in a dictionary

list(myCat.key())
list(myCat.values())
list(myCat.items()) # this lists the dictionary keys


#you can use these methods in for loops

for k in myCat.keys():
    print(k)

#this should print out all the keys in the myCat dictionary

