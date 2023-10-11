#guess the number game
#importing the random module
import random

print('Hello, what is your name?')
name = input()

print('Hello, ' + name + ', I am thinking of a number between 1 and 20')
#creates a new variable called secret number. you call the modules function `randint` and specify the range
secretNumber = random.randint(1, 20)

#create a for loop
for guessesTaken in range(1, 7):
    print('Take a guess.')
    #we need to convert the guess to an integer because we want it to be a number between 1-7
    guess = int(input())
    #loop statement. the break is for the correct guess.
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed the number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope! WRONG! The number was ' + str(secretNumber) + '.')

print('You took ' + str(guessesTaken) + ' guesses.')