#Yarielis Diaz Colon 
#SE1116.02
#W6D2 Lab 6
#2-17-2025 

#PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a
#small airplane with seat numbering as follows.

# imports ---------
import csv

#functions ------------
def display():
  dataFile
#lists -----------
row = []
secA = []
secB = []
secC = []
secD = []

dataFile = [
    row,
    secA,
    secB,
    secC,
    secD,
]

#within the file

with open ("week8/lab6.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        dataFile.append(rec)


print("\n\nDATA FILE (2D LISTS[][]):")
for i in range(0,len(dataFile)):
    #accessing each list within the 2D list
    print(f"INDEX {i} of 'DataFile': {dataFile} ")
    for j in range(0,len(dataFile[i])):
        #accesssing each value within the list currently looked at from outter loop
        print(f"INDEX {i} and value DataFile[{j}]: {dataFile[i][j]}")

print(dataFile)

