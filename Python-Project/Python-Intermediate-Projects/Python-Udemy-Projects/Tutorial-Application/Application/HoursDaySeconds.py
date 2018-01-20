__author__ = 'pthapax'
print("Hello welcome to the program!!!!")
number=input("Please enter a integer: ")
number_int=int(number)
one_day_in_seconds= 60*60*24
#Calculate Day

days= number_int//one_day_in_seconds
remaining_seconds=days%one_day_in_seconds

#Calculate Hours
hours_seconds = remaining_seconds//(60*60)
remaing_seconds_day =remaining_seconds%(60*60)

#calculate minutes
minutes= remaing_seconds_day//60

# Calculate seconds
seconds= minutes%60

print(days,"days" ,hours_seconds,"hours", minutes,"minutes",seconds,"seconds")
