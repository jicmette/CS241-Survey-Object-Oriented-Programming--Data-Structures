import random
from random import randint

print("Welcome to the number guessing game!")
the_seed_value = input("Enter random seed: ")
random.seed(the_seed_value)

print()
def game1():
    num = random.randint(1,100)
    guess = 1
    attempts = 1

    while guess != num:
        guess = input("Please enter a guess: ")
        guessnum = int(guess)
        
        if guessnum > num:
            print("Lower\n")
            attempts += 1
            
        elif guessnum < num:
            print("Higher\n")
            attempts += 1 
            
        elif guessnum == num:
            print("Congratulations. You guessed it!")
            print("It took you {} guesses.\n".format(attempts))
            return again()
            
def again():
    while True:
        if input("Would you like to play again (yes/no)? ") == "yes":
            print()
            return game1()
        else:
            print("Thank you. Goodbye.")
            break
            
game1()