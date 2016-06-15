__author__ = 'pthapax'
# This program will tell you How much you made per week based on the hours

print("Hello!!!! I am here to assist you in calculating your pay check")
hours_worked =int(input("Please enter the number of hours you worked: "))
total_Amount=0
Pay_40_hrs=int(8)
Pay_extra_42_50=int(9)
Pay_above_50 =int(10)

if hours_worked <0 or hours_worked>168:
    print("INVALID")
elif hours_worked <= 40:
    total_Amount= hours_worked*Pay_40_hrs
    print("Your Pay is : "+str(total_Amount))
elif hours_worked <=50:
    total_Amount =(40*Pay_40_hrs)+((hours_worked-40)*9)
    print("Your Pay is : "+str(total_Amount))
else:
    total_Amount=(40*Pay_40_hrs)+(10*Pay_extra_42_50)+((hours_worked-50)*10)
    print("Your Pay is : "+str(total_Amount))
print("Thank you for using hours calculator ")





