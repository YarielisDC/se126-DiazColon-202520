#Yarielis Diaz Colon 
#SE1116.02
#W3D2 Lab 3
#1-27-2025 

#------- IMPORTS ---------
import csv
#------------------------

#------------ FUNCTIONS ------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "EROR"
    return let #'let' value replaces the function call in hte main executing code
#------------ LISTS ----------------------------------
fName = []
lName = []
test1 = []
test2 = []
test3 = []


#------ -------- MAIN EXECUTING CODE -----------------------------
with open("week4/class_grades-2.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file: 
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))


#-------------OUT OF THE FILE--------------------
num_avg = [] # Making a list so it stores the data into the 'num_avg' list
letter_avg = [] #Making a list storing the data of the avg grades to a letter grades. 

for i in range(0,len(fName)):  
    a = (test1[i] + test2[i] + test3[i])/ 3 #does the math for averages 
    num_avg.append(a) #stores the total avg into the num_avg list
    
    l = letter(a) # a variable for the function that also holds the data for the letter(a) function 
    letter_avg.append(l) #then the results from l or the letter function is stored into let_avg list

#The final displays 
print(f"{'FNAME':10}  {'LNAME':10}  {'T1':3}  {'T2':3} {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("-----------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:10}  {lName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.2f} {letter_avg[i]}")
print(f"There are {len(fName)} students in the file. ")

#SEQUENTIAL SEARCH 

print("\n\nWelcme to the Student Search Program\n\n")

answer = input("Would you like to begn searching? [y/n]: ").lower()

while answer == "y":
    #SEARCH MENU LIST
    print("\tSEARCH MENU OPTIONS")                   
    print("1. Search by LAST name")                  
    print("2. Search by FIRST NAME")               
    print("3. Search by LETTER GRADE")
    print("4. Exit ")                                 
    
    search_type = input("Enter your search type: ").lower()

    if search_type == "1":
        print("Last Name Search")
        found = -1 
        search_Lname = input("Enter the last name you would like to search: ")

        for i in range(0, len(lName)):
            if search_Lname.lower() == lName[i].lower():
                found = i 
        if found != -1:
            #last name FOUND!
            print(f"Your search for {search_Lname} was FOUND! Here is their data: ")
            print(f"{fName[found]:10}  {lName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {letter_avg[found]}")
        else: 
            #NOT found
            print(f"Your search for {search_Lname} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
    
    elif search_type == "2":
        found = "x"
        print("\nFirst Name Search")
        search_FN = input("Enter the FIRST name you would like to search: ")
        
        for i in range(0, len(fName)):
            if search_FN.lower() == fName[i].lower():
                found = i
            
        if found != "x":
            print("Your search entry was found!")
            print(f"{fName[found]:10}  {lName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {letter_avg[found]}")
        else: 
            print("Your entry was not found")
    
    elif search_type == "3":
        found = []
        search_lg = input("Please enter the letter grade you would like to find: ")
        
        for i in range (0,len(letter_avg)):
            if search_lg == letter_avg[i]:
                found.append(i)
                print(f"Found a {search_lg} grade in INDEX {i}")
        
        if not found:
            print("Your search entry was not found")
        else:
            print("Your search entry was found!")
            for i in range(0,len(found)):
                print(f"{fName[found[i]]:10}  {lName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {letter_avg[found[i]]}")
        

    elif search_type == "4":
        print("EXIT")
        answer = "o"
        print("Goodbye!")

