from tkinter import *
import sys
import datetime
import pyodbc

window =Tk()
"""Grid for Input Container"""
label_1 = Label(window,text='Diagnosis Name')
label_1.grid(row=0,column=0)

label_2 = Label(window,text ='DiagnosisMasetSK')
label_2.grid(row=0,column=2)

label_3 = Label(window,text='Generic Name')
label_3.grid(row=1,column=0)

label_4= Label(window,text='DrugMasteSk')
label_4.grid(row=1,column=2)

"""Setting Parameter Boxes """
text_DiagName = StringVar()
entry_1 = Entry(window,textvariable=text_DiagName)
entry_1.grid(row=0, column=1)

text_DiaSk = StringVar()
entry_2 = Entry(window,textvariable = text_DiaSk)
entry_2.grid(row=0, column = 3)

text_GenericName = StringVar()
entry_3 = Entry(window,textvariable = text_GenericName)
entry_3.grid(row=1, column =1)

text_DrugMasterSk = StringVar()
entry_4 = Entry(window,textvariable=text_DrugMasterSk)
entry_4.grid(row=1,column=3)


#Creating a Box below the Input Object

listBox1 = Listbox(window,height=6,width=35)
listBox1.grid(row=2,column=0,rowspan=6,columnspan=2)

# Creating a ScrollBar
Sb1 = Scrollbar(window)

#Positioning the ScrollBar
Sb1.grid(row=3, column =2, rowspan=5)

#Configuring Scrollbar to the listBox
listBox1.configure(yscrollcommand=Sb1.set)
Sb1.configure(command=listBox1.yview)

""" Creating Buttons on the Left"""
b1= Button(window,text='View All', width =12)
b1.grid(row=2,column=3)

b2= Button(window,text='Search Entry',width=12)
b2.grid(row=3,column=3)

b3= Button(window, text='Add', width=12)
b3.grid(row=4,column=3)

b4= Button(window,text='Update',width=12)
b4.grid(row=5, column=3)

b5 = Button(window,text='Delete',width=12)
b5.grid(row=6,column=3)

b6= Button(window, text='Close',width =12)
b6.grid(row=7, column=3)



""" This Ends the program"""

window.mainloop()
