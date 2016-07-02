# This is a small program to guess a number
import random

name = raw_input("Hello !! What is your name???")
secretNumber = random.randint(1,20)
print(secretNumber)
#print(secretNumber)

print("Well " + name + " I am thinking of a number betwee 1 and 19 , Can you take a gues??? ")

guess_taken=1
while guess_taken <= 6:
    number_guessed = int(raw_input("What is the number????"))   
    if number_guessed > secretNumber:
        print("Guess Something low ")
        guess_taken =guess_taken + 1
    elif number_guessed < secretNumber:
        print("Guess Something higher ")
        guess_taken =guess_taken + 1
    else:
        break


if (number_guessed == secretNumber):
    print("Good Job "+ name +"!!!!")
else:
    print("Nope I was thinking of " + str(secretNumber))






# for guessTaken in range(1,7):
#     guess =int(raw_input())

#     if guess > secretNumber:
#         print("Its too high, guess something lower")
#     elif guess<secretNumber:
#         print("Its a bit low , guess something bigger")
#     else:
#         break




