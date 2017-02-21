# import  csv
#
# file_name_csv = "Chapter.csv"
# ACCESSMODE = 'r'
#
# with open(file_name_csv,ACCESSMODE) as CSVfile:
#     open_file_name = csv.reader(CSVfile)
#     for eachline in open_file_name:
#         for currentline in eachline:
#                 print(currentline)
#                 print(eachline)
#
#
# print("Reading Complete")
# print("Load comlpete")
#
# # Lists : Creating a list
# my_list =['Hello',5.6,100,'true']



# Value of y

# value_x =input("Enter any number: ")
#
# value_Y =int(value_x)**2 -12*int(value_x) +11
# print(value_Y)


# # Day of Week: Allow the user to pic the day for three time
# ask_date =1
# while ask_date <=3:
#
#     day_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#     day=int(input("Please enter number between 1 and 7 to find which day of the week: "))
#     print(day_week[(day-1)])
#     ask_date +=1
# print("End of Script!! Thank you for using the Program")

#

# # ask User for age program
# print("Hello welcome to the age display program ")
#
# user_age=int(input("Please enter your age: "))
#
# if user_age <=0:
#     print("UNBORN")
# elif user_age > 0 and user_age <=150:
#     print("ALIVE")
# else:
#     print("VAMPIRE")


# Division
n =int(input("Please enter a positive integer: "))
two_var= int(n%2)
three_var =int(n%3)

# start the Program
if two_var==0 and three_var==0 :
    print("BOTH")
elif (two_var==0 and three_var !=0) or (two_var !=0 and three_var==0):
    print("ONE")
else:
    print("NEITHER")






