#Yarielis Diaz Colon
#SE116.02
#W3D2 in Class lab
#1/21/25

#----IMPORTS------------------------------
import csv 

computer = []


year = []

#---connected to the file ----------------------
print(f"{'Type':9} {'Brand':9}   {'CPU':5}  {'RAM':5}  {'1st Disk':10}  {'NO HDD':8}  {'2nd Disk':10}  {'OS':5} {'YR':4}\n")
with open ("week2/filehandling.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        computer_ = rec[0]   #0
        
        if computer_ == "D":
            computer.append("Desktop")
        
        else:
            computer.append("Laptop")
        
        brand = rec[1]      #1
        cpu = rec[2]        #2
        ram = rec[3]        #3
        disk1 = rec[4]      #4
        hdd = rec[5]        #5
        os = rec[6]         #6
        year.append(int(rec[7]))        #7


        if brand == "DL":
            brand = "Dell"
        
        if brand == "GW":
            brand = "Gateway"
        
        if hdd == "1":
            print(f"{computer:9} {brand:9}   {cpu:5}  {ram:5}  {disk1:10}  {hdd:8}  {'-----':10}  {os:5} {yr:4}")
        
        if hdd == "2":
            yr = rec[8]
            os = rec[7]
            disk2 = rec[6]
            hdd = rec[5]
            print(f"{computer:9} {brand:9}   {cpu:5}  {ram:5}  {disk1:10}  {hdd:8}  {disk2:10}  {os:5} {yr:4}")
#disconnected from file - using LiSTS to process
desktop_over = 0

for i in range(0,len(computer)):
    if computer[i] == "Desktop" and year[i] <= 16:
        desktop_over += 1
     