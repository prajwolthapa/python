import random
import os
import string

def genlowercase():
    letterL =random.choice(string.ascii_lowercase)
    return letterL


def genUpperCAse():
    letterU =random.choice(string.ascii_uppercase)
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
    return lowecaseletter

def CreateUpprChr():
    loop_count = 0
    UpperCase =""
    while loop_count < 5:
        UpperCase  = UpperCase + genUpperCAse()
        loop_count = loop_count +1
    return UpperCase

def CreateNumber():
    loop_count = 0
    num =""
    while loop_count < 2:
        num  = num + str(genNumber())
        loop_count = loop_count +1
    return num

x = CreateUpprChr()+CreateLoerChr()+CreateNumber()
print(x)
