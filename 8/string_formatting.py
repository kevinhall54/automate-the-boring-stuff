#string formatting

#adding two strings is as simple as:

#'hello ' + 'world', this will give you 'hello world'. 

name = 'Alice'
place = 'Main St'
time = '6 PM'
food = 'french fries'

'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food

#the above is long and can be misread. you can do string interpolation by doing %s per string
#and then making a comma delimited list of variables. see the following.

'Hello %s, you are invited to a party at %s at %s. Please bring %s' %s (name, place, time, food)

#this will do the same as the first string but its easier to type out and read.
