#W2D1 Text File Handling - Introduction

#STEP 1: import the csv (comma separated value) library 
import csv

total_records = 0 #the total of records (rows) in the file


#STEP 2: 
#connecting to the file's path - switch \ to / 
print("f\n{'NAME' :10} \t {'NUM' :3} \t {'COLOR'}")

#HEADER PRINT
print("-------------------------------------")
#----connected to file--------------------------------------------------------
with open("text_files/simple.csv") as csvfile:
    #indent 1 level! (new block)

    #allow proccessor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        total_records += 1
        print(record) #the list view of each record (row)
       
        name = record[0]
        number = record[1]
        color = record[2]

        
        print(f"{name:10} \t {number:3} \t {color}")
#------disconnected from file------------------------------------------
print(f"\nTOTAL RECORDS: {total_records}\n")
