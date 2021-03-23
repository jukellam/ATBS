# A game to guess a number
import random

print('What is your name, sir?')
name = input()

print('Hello, ' + name + ', I am thinking of a number between 1 and 20! Can you guess it?')
secretnumber = random.randint(1, 20)

for guessestaken in range(1, 7):
    guess = int(input())

    if guess < secretnumber:
        print('Your guess is too low')
    elif guess > secretnumber:
        print('Your guess is too high.')
    else:
        break #If the guess is correct
    print('Guess again!')

if guess == secretnumber:
    print('Well done, ' + name + '! You are good at guessing! You guessed my number in ' + str(guessestaken) + ' guesses.')
else:
    print('You took ' + str(guessestaken) + ' guesses, I am tired of this game. My secret number was ' + str(secretnumber) + '.')