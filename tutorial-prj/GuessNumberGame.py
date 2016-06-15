# This is a small program to guess a number
import random
print("Hello !! What is your name???")
name=input()
secretNumber=random.randint(1,20)
print("Well" + name + "I am thinking of a number betwee 1 and 19")

for guessTaken in range(1,7):
    print("Take a gues!!!")
    guess =int(input())

    if guess > secretNumber:
        print("Its too high, guess something lower")
    elif guess<secretNumber:
        print("Its a bit low , guess something bigger")
    else:
        break

if (guess== secretNumber):
    print("Good Job "+ name +"!!!!")
else:
    print("Nope I was thinking of " + str(secretNumber))




