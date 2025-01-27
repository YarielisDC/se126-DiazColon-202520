#W4D1 - Sequential Search





#------IMPORTS---------------------------------------------------
import csv

#------FUNCTIONS-----------------------------------------------
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

#---MAIN EXECLUDING CODE------------------------------------------

#create empty lists to hold the file data
fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("week4/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        #append the file data into appropiate lists
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file -- can still access the stored data via the lists

#process the list data to calc an avg score for each student, and file a letter grade equivalent 

num_avg = [] #will hold each student's numeric average of test scores
let_avg = [] #will hold each student's letter average of test schores

for i in range(0, len(fName)):
    a = (test1[i] + test2[i]+ test3[i]) / 3
    #add average to num_avg list
    num_avg.append(a) #can also do: num_avg.append((test[i] + test2[i] + test3[i] / 3 ))

    l = letter(a) #return value to the letter() stored to 1
    let_avg.append(l) #can also do: let_avg.append(letter(a))

#process the lists to display all student data to the user
print(f"{'FNAME':10}  {'LNAME':10}  {'T1':3}  {'T2':3} {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("-----------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:10}  {lName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.2f} {let_avg[i]}")
print("-------------------------------------------------------------------------------------")
print(f"There are {len(fName)} students in the file. ")

#Write a progtam that allows a user to repeatedy search for a student 

print("\n\nWelcme to the Student Search Program\n\n")

answer = input("Would you like to begn searching? [y/n]: ").lower

while answer == "y":
    
    #get search type from user
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")
    
    search_type = input("enter your search type")
    if search_type == "1":
        print("SEARCH BY LAST NAME")
        
        #get search item from user
        found = -1 #invalid index number, will use to check later to see if a student has been found
        
        #get search from user
        search_name = input("Enter the LAST NAME of the student you are searching for")

        #perfrom search
        for i in range(0, len(lName)):
            #the FOR LOOP allows for the "sequence" part -> from beginning to end
                if search_name.lower() == lName[i].lower():
                    #the IF STATEMENT allows for the "search" part
                    found = i #make found the current index, can be used later to display 
      
    elif search_type == "2":
        print("\tSEARCH BY LETTER GRADE")
        found = []
        search_grade = input("Enter th LETTER GRADE of the students you are searching for: ")
        for i in range(0, len(let_avg)):
            if search_grade.upper() == let_avg[i]:
                found.append() #add the current index (found), can be used later to display 

    elif search_type == "3":
        print("SEARCH BY LETTER GRADE")
    #display results
    if not found: #the list is empty

        #last name has been found! we can display data 
        print(f"Your search for {search_grade} was *NOT* FOUND!")
        print(f"This is cAsE sEnSiTiVe program - check your spelling and casing and try again. ")
      

    else:
        print(f"Your search for {search_grade} was FOUND!")
        for i in range(0, len(found)):
            print(f"{fName[found[i]]:10}  {lName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.2f} {let_avg[found[i]]}")
    

    #build a way out of the loop
    if search_type == "1" or search_type == "2": 
        answer = input("Would you like to search again? [y/n]").lower