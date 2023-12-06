# Simple guessing game
import random

guesses = 1
tries = 6
number = random.randint(1,20)

name = input("Hello. What is your Name? ")
print("Hello, " + name + " I am thinking of a number between 1 and 20.")

while (guesses <= tries): 
    guess = int(input("Take a guess. "))
    if ( guess > number):
        print("Your guess is high.")
        guesses = guesses + 1
    elif ( guess < number): 
        print("Your guess is low.")
        guesses = guesses + 1
    else :
        print("Good job, " + name + "! You guessed my number in " + str(guesses) + " gusses!")
        break

if (guesses > tries):
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")
