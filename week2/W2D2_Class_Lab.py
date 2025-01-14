#Yarielis Diaz Colon
#SE116.02
#W2D2 in Class lab
#1/13/2025

#W2D2 - Text File Handling Review w/ filters!

#Program Prompt:


#VARIABLE DICTIONARY:

#--IMPORTS-----------------------------
import csv

#--FUNCITIONS--------------------------
def difference(people, max_cap):
    '''this function is passed 2 valies and returns the differnce between them'''
    diff = max_cap - people
    return diff
#--MAIN EXECUTING CODE--------------------------------------

#Initialize needed counting variables
total_rec = 0 
rooms_over = 0 
print(f"{'Name':20}   {'MAX':5}     {'PPl':5}    {'OVER'}") #FIELD HEADERS for display
print("------------------------------------------------------")
#-----connected to file---------
with open("week2/classLab2.csv") as csvfile:
    #we must indent one level while "connected to file"
    
    file = csv.reader(csvfile)
    
    for rec in file:
        #below code occurs for every record (row) in the file (text file!)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])
        ppl = int(rec[2])
        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display rooms that over capacity (remaining is negative)
        if remaining < 0:
            rooms_over += 1 
            print(f"{name:20}  {max:5}   {ppl:5}   {abs(remaining):5}")
        total_rec += 1 
#-----connected to file----------


#display final data (counting vars)
print(f"\nRooms currently OVER CAPACITY: {rooms_over}")
print(f"Total Rooms in file: {total_rec}\n\n")