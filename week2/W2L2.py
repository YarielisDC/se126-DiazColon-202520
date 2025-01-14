# Yarielis Diaz Colon
#SE116.02
#W2D2 in Class lab
#1/14/2025

#Program Prompt: 

#VARABLE DICTIONARY: 


#----IMPORTS------------------------------
import csv 

#---connected to the file ----------------------
print(f"{'Type':10}    {'Brand':10}   {'CPU':5}     {'RAM':5}     {'1st Disk':7}    {'NO HDD':5}      {'2nd Disk':7}    {'OS':5}  {'YR':4}   ")
with open ("week2/filehandling.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        computer = rec[0]   #0
        brand = rec[1]      #1
        cpu = rec[2]        #2
        ram = rec[3]        #3
        disk1 = rec[4]      #4
        hdd = rec[5]        #5
        os = rec[6]         #6
        yr = rec[7]         #7
        if computer == "D":
            computer = "Desktop"
        
        else:
            computer = "Laptop"
        
        if brand == "DL":
            print(f"{'Dell':7}")
        
        elif brand == "GW":
            print(f'{'Gateway':7}')
        
        elif hdd == "1":
            print(f"{computer:10}   {brand:10}  {cpu:5}     {ram:5} {disk1:7}   {hdd:5}     {os:5}      {yr:4}")
        
        #if hdd == "2":

