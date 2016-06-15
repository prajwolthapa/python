# loop
for i in range(10):
    if i ==5:
        {
            print("The value of i is 5 and we still have 4 more to go before the loop ends")
        }
        print("Loop ends for now")
    print("Hello World " + (str(int(i))))

#Loop
cats=input("How many cats do you have???")
try:
    if int(cats) >=4:
        print("that is a lot of cats")
    else:
        print("Ummm, not to may huh!!!")
except ValueError:
    print("Please enter a number for the program to work. Thank You!!!")