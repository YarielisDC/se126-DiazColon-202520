#Yarielis Diaz Colon 
#SE1116.02
#W3D2 Lab 3
#1-27-2025 

#------- IMPORTS ---------
import csv

#------------------------

#------------ LISTS ----------------------------------
fName = []
lName = []
test1 = []
test2 = []
test3 = []


#------ MAIN EXECUTING CODE -----------------------------
with open("week4/class_grades-2.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file: 
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
