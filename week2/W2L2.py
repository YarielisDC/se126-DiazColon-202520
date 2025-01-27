# Yarielis Diaz Colon
#SE116.02
#W2D2 in Class lab
#1/14/2025

#Program Prompt: 

#VARABLE DICTIONARY: 


#----IMPORTS------------------------------
import csv 

#---connected to the file ----------------------
print(f"{'Type':9} {'Brand':9}   {'CPU':5}  {'RAM':5}  {'1st Disk':10}  {'NO HDD':8}  {'2nd Disk':10}  {'OS':5} {'YR':4}\n")
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
            brand = "Dell"
        
        if brand == "GW":
            brand = "Gateway"
        
        if hdd == "1":
            print(f'{computer:9} {brand:9}   {cpu:5}  {ram:5}  {disk1:10}  {hdd:8}  {"------":10}  {os:5} {yr:4}')
        
        if hdd == "2":
            yr = rec[8]
            os = rec[7]
            disk2 = rec[6]
            hdd = rec[5]
            print(f'{computer:9} {brand:9}   {cpu:5}  {ram:5}  {disk1:10}  {hdd:8}  {disk2:10}  {os:5} {yr:4}')