#Yarielis Diaz Colon
#SE116.02
#W3D2 in Class lab
#1/21/25
#----IMPORTS------------------------------
import csv
computer = []
year = []
desktop_over = 0
laptop_over = 0 
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
        
    
        
        if brand == "DL":
            brand = "Dell"
       
        if brand == "GW":
            brand = "Gateway"
       
        # CHANGE 2: Add the year handling here
        if hdd == "1":
            os = rec[6]         #6
            year.append(int(rec[7]))   # Add year for single HDD case
            print(f'{computer_:9} {brand:9}   {cpu:5}  {ram:5}  {disk1:10}  {hdd:8}  {"-----":10}  {os:5} {rec[7]:4}')
       
        if hdd == "2":
            disk2 = rec[6]
            os = rec[7]
            yr = rec[8]
            year.append(int(rec[8]))   # Add year for double HDD case
            print(f"{computer_:9} {brand:9}   {cpu:5}  {ram:5}  {disk1:10}  {hdd:8}  {disk2:10}  {os:5} {yr:4}")

#disconnected from file - using LiSTS to process

for i in range(0,len(computer)):
    if computer[i] == "Desktop" and year[i] <= 16:
        desktop_over += 1 
    
        print(f"To replace it will cost $ ")


#for i in range(0,len("Laptop")):
    #if laptop_[i] == "Laptop" and year [i] <= 16:
        #laptop_over += 1