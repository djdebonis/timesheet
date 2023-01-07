import os

#creating timesheet for work
#asking user for previous file or new one
initiate = input("Would you like to create a new timesheet or edit an existing timesheet? /n 1. For New /n 2. For existing")
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



r
