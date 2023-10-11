#defintes function
def div42by(divideBy):
    return 42/ divideBy

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

#after the divide by 0, the program crashes and no longer does the last print line. can attempt to circumvent this with a try and/or except statement.

#defintes function
def div42by(divideBy):
    try:
        return 42/ divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# when this second program is ran, it runs through the entire thing and doesnt crash after the third print statement.


#example of input validation

print('How many cats do you have?')
numCats = input()
if int(numCats) >= 4:
    print('That is a lot of cats')
else:
    print('That is not a lot of cats')

#when someone types in a string rather than an integer, it will blow up. You can put in an except statement. Instead of returning an error for the value, it will 
#return the print statement defined for ValueError.


print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not a lot of cats')
except ValueError:
    print('You did not enter a numeric number')
