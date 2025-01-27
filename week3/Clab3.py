import csv 

computer = []
brand = []
cpu = []
ram = []
disk1 = []
hdd = []
disk2 = []
os = []
year = []
#KNOWN VARIABLES
laptop_over = 0
desktop_over = 0
cost = 0 
cost2 = 0 

#---connected to the file ----------------------
print(f"{'Type':10} {'Brand':10} {'CPU':5} {'RAM':5} {'1st Disk':10} {'HDD':10} {'2nd Disk':10} {'OS':5} {'YR':5}\n")

with open ("week2/filehandling.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        cpu.append(rec[2])   
        ram.append(rec[3])  
        disk1.append(rec[4]) 
        hdd.append(int(rec[5]))
        os.append(rec[6])    
        
       
        if rec[0]== "D":
            computer.append("Desktop")
       
        else:
            computer.append("Laptop")
       
        if rec[1] == "DL":
            brand.append("Dell")
        
        if rec[1] == "GW":
            brand.append("Gateway")
        if rec[1] == "HP":
            brand.append("HP")
            
        if int(rec[5]) == 1:
            disk2.append("----")
            os.append(rec[6])         
            year.append(int(rec[7]))    
        
        else:
            disk2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])
          
        

#disconnected from file - using LiSTS to process
    for i in range(0,len(computer)):
            print(f'{computer[i]:10} {brand[i]:10} {cpu[i]:5} {ram[i]:5} {disk1[i]:10} {int(hdd[i]):10} {disk2[i]:10} {os[i]:5} {year[i]:5}')

for i in range(0,len(year)):
    if int(year[i]) <= 16:
        if computer[i] == "Desktop":
            desktop_over += 1
            cost = desktop_over * 2000

for i in range(0,len(year)):
    if int(year[i]) <= 16:
        if computer[i] == "Laptop":
            laptop_over += 1 
            cost2 = laptop_over  * 1500
#Final Display       
print(f"To replace {int(desktop_over)} it will cost ${cost}")
print(f"To replace {int(laptop_over)} it will cost ${cost2}")