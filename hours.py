import csv
import os
import pathlib
from csv import writer

import datetime as dt
import pandas as pd

#creating timesheet for work
#asking user for previous file or new one
initiate = input("Would you like to create a new timesheet or edit an existing timesheet? \n 1. For New \n 2. For existing")
#if the user wants a new file
if initiate == "1":
    newfile = input("what would you like the file name to be?  :") +".csv"
    location = input("where would you like the file to be saved?/n note if you want it in the default directory hit 1")
#if the user doesnt want a certain location
    if location == "1":
            #opening file with name given with x to make sure theres no write over
        newopen = open(str(newfile) , +x)
        #opening the file in append mode to ensure no data is lost.
        fa = open(str(newfile), +a)
        #asking user for hours worked.
        hours = int ("how many hours have you worked this shift?")
        fa.write(int(hours))
        fa.close()
        
if initiate == "2":
    print("Select which file you'd like")
    files = sorted(pathlib.Path('.').glob('**/*.csv'))
    files_tup = [((str(item) + ". "),element) for item,element in enumerate(files)]
    [print((i[0] + str(i[1]) + "\n")) for i in files_tup]
    file = ''
    
    while True:
        selection = int(input("Which file would you like to select? Enter integer only"))
        try:
            file_tup = files_tup[selection]
            file = file_tup[1]
            break
        except IndexError:
            print("Oops!  That was no valid number.  Try again...")
    
    data = pd.read_csv(file, index_col = False)
    
    columns = [col for col in data.keys()]
    print("Columns:")
    print(columns)
    
    new_row = []
    
    date = input("Enter date YYYY-mm-dd format")
    
    new_row.append(date)
    
    choice = input("Would you like to input time by hours or total time? \n 1. Hours \n 2. Total Time \n")
    
    while True:
        if choice == '1':
            time = int(input("Enter hours spent"))
            new_row.append(time)
            
            
            
            
            
            break
        
        elif choice == '2':
            
            break
            
                  ]
    
    
#     with open(file, 'a') as f_object:
#         writer_object = writer(f_object)
        
    
    
    
    
    
