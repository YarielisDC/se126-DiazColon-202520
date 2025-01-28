#W3D2 - SequentialSearch Review + Creating & Writing to Text Files

#Program Prompt: IN the W4D2 demo, we will review utilizing sequential search for simple singular and muli returns. We will then create and write data to text file using Python.

#--------------- Imports -------------------------------------
import csv
#-------------------------------------------------------------

#--------------- Functions ------------------------------------


#--------------- Main Executing Code ----------------------------

#creating empty lists - one for reach field, 
dragons = []    #field 0
riders = []     #field 1
count = []      #field 2
color1 = []     #field 3
color2 = []     #field 4

with open ("week4\dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])
        
        if rec[2] == "2":
            color2.append(rec[4])
        else:
            color2.append("---")
#---------- disconnected from file --------------------

#process the lists to display data to the console
print(f"{"DRAGONS":15} {'RIDERS':30} {'#':3} {'1COLOR':8} {'2COLOR':8}")
print("----------------------------------------------------------------------")

for i in range(0, len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]}")
print("--------------------------------------------------------------------------")


#SEARCH FOR A SPECIFIC DRAGON
#step 1: set-up and gain of search
found = "x"
search = input("Which dragon are you looking for:")

#step2: perform search ---> for loop w/ a if statement
for i in range(0,len(dragons)):
    if search.lower() in dragons[i].lower():
        #hold onto the found location of our searched-for value
        found = i
#step 3: filter and display results
if found != "x": #search was found!
    print(f"Your search for {search} was FOUND!:")
    print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]}")
else:
    print(f"Your search for {search} was NOT FOUND!")

#SEARCH FOR A COLOR SET
found = []
search = input("Enter the dragon color are you looking for: ")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)













if not found: #if the found list is empty
    print(f"Your search for {search} was NOT FOUND!")

else:
    print(f"Your search for {search} was FOUND!:")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15} {riders[found[i]]:30} {count[found[i]]:3} {color1[found[i]]:8} {color2[found[i]]}")

#WRITE SOME DATA TO A NEW FILE
file = open('week4/test.csv', 'w')
for i in range(0,len (dragons)):
    file.write(f" {dragons[i]}, {riders[i]}\n")
file.close()