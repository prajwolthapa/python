import random
import os
import string

def genlowercase():
     letterL =random.choice(map(chr, range(97,123)))
     return letterL


def genUpperCAse():
    letterU =random.choice(map(chr, range(65,91)))
    return letterU

def genNumber():
    number_random = random.randint(0,9)
    return number_random

def CreateLoerChr():
    loop_count = 0
    lowecaseletter =""
    while loop_count < 5:
        lowecaseletter  = lowecaseletter + genlowercase()
        loop_count = loop_count +1
    print (lowecaseletter)

def CreateUpprChr():
    loop_count = 0
    upper =""
    while loop_count < 4:
        Upper  = upper + genUpperCAse()
        loop_count = loop_count +1
    print (upper)

def CreateNumber():
    loop_count = 0
    num =""
    while loop_count < 3:
        num  = num + str(genNumber())
        loop_count = loop_count +1
    print (num)

password =  genNumber()
print(password)
