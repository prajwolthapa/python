import os
from datetime import datetime
import time
import logging

file_name='directory.txt'
access_mode = 'r'


def directory():
    with open(file_name,access_mode,) as dirpath:
        return  dirpath.readline()

def deletelogfile():
#variable and folder properties
    working_directory = directory()
    file_directory = os.listdir(working_directory)

# Get time stamp details for each file in the folder;
    for eachfiles in file_directory:
        exp_date = 0
        current_date = datetime.now()
        cur_date_to_string = current_date.strftime(" %d %b %Y ")# converting into a string
        curr_date_dateformat = datetime.strptime(cur_date_to_string," %d %b %Y ").date() # Converting to date format

        current_time_float = os.path.getctime(working_directory+'\\'+eachfiles)
        filename,extension = os.path.splitext(working_directory+'\\'+eachfiles) #Capturing File Names and their extension

        real_date_time= time.strftime(" %d %b %Y ", time.gmtime(current_time_float))
        file_date = datetime.strptime(real_date_time," %d %b %Y ").date()

# We now handle the logic to work with files that has past expiration date
        number_days_file_in_directory= (curr_date_dateformat - file_date).days

# We check if the file extension is a logfile
        if extension =='.log':
            # If the test passes we then check to see if it fits the number of days the file has been there
            if number_days_file_in_directory >= exp_date:
               x= os.remove(working_directory+'\\'+eachfiles)
               logging.info("Deleting files......")
            else:
                pass
        else:
            pass
