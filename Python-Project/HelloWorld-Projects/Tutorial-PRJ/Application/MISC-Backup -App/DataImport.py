import csv
# Playing around with data: reading a file and writing a file,
# recList=input("Number of Guests")
# for i in range(int(recList)+1):
#     Name= input("What is you Name??? ")
#     Age= input("What is your age???")
#     Address= input("City")
#     fileName="Demo.txt"
#     accessMode="a"
#     myFile =open(fileName,mode=accessMode)
#     myFile.write(Name+' ,'+ Age+' ,'+  Address +" \n")
#     myFile.close()
# print("File written successfully")



# Reading from a csv file with csv module
mode_access="rU"
file_name="Fl_insurance_sample.csv"
with open(file_name,mode_access) as my_csv_file:
    file_content=csv.reader(my_csv_file)

    for current_row in  file_content:
        if 'MARION COUNTY' in current_row:
            print("Shows alll MArion County related Data",current_row)

