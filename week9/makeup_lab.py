#Yarielis Diaz Colon & Natalie G 
#SE116.02 
#W9D2 Makeup lab 
#3-4-2025 

#PROGRAM PROMPT: MENU SEARCH FROM STUDENT.txt 

#imports 
import csv 

  

#lists  
id = [] 
lastName = [] 
firstName = [] 
class1 =[] 
class2 = [] 
class3 = [] 

#functions 
def menu(): 
    print("\nSearch Menu") 
    print("1. See all Student's reports") 
    print("2. Search for a Student ID") 
    print("3. Search for a student's last name") 
    print("4. View class Roster") 
    print("5. EXIT PROGRAM ") 

def swap(index,listName): 
    temp = listName[index] 
    listName[index] = listName[index + 1] 
    listName[index + 1 ] = temp 

#within the file 
with open("week9/students.csv") as csvfile: 
    file = csv.reader(csvfile) 
    
    for rec in file: 

        id.append(rec[0]) 
        lastName.append(rec[1]) 
        firstName.append(rec[2]) 
        class1.append(rec[3]) 
        class2.append(rec[4]) 
        class3.append(rec[5]) 

# MAIN CODE BELOW 
answer = "y"
while answer == "y": 
    print("\nWelcome to the search program\nPlease select options [1-5]") 
    menu() 


    search = input("What would you like to search by? ") 

    if search not in ["1", "2", "3","4","5"]: 

        print("***INVALID ENTRY!***\nPlease try again") 


    elif search == "1":
        print(f"{'ID':8} {'LNAME':10} {'FNAME':9} {'CLASS1':9} {'CLASS2':9} {'CLASS3':9}")
        print("---" * 50)
                
        for i in range(len(id)):
            print(f"{id[i]:8} {lastName[i]:10} {firstName[i]:9} {class1[i]:9} {class2[i]:9} {class3[i]}")
        print("---" * 50)

    elif search == "2":
        min = 0
        max = len(lastName) - 1
        mid = int((min + max) / 2)
        
        search = input("Please enter the student ID you are looking for: ")
        while min < max and search != id[mid]:
            if search < id[mid]:
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
            
            if search in id[mid]:
                print(f"{'ID':8} {'LNAME':10} {'FNAME':9} {'CLASS1':9} {'CLASS2':9} {'CLASS3':9}")
                print("---" * 50)
                print(f" {id[mid]:8} {lastName[mid]:10} {firstName[mid]:9} {class1[mid]:9} {class2[mid]:9} {class3[mid]:9}")
                print("---" * 50)
            else:
                print(f"Your search for {search} was not found") 
    

    elif search == "3":
        min = 0
        max = len(lastName) - 1
        mid = int((min + max) / 2)

        search = input("Please enter the last name you are looking for: ")

        
        while min < max and search.lower() != lastName[mid].lower():
            if search.lower() < lastName[mid].lower():
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
        
        if search.lower() in lastName[mid].lower():
            print(f"{'ID':8} {'LNAME':10} {'FNAME':9} {'CLASS1':9} {'CLASS2':9} {'CLASS3':9}")
            print("---" * 50)
            print(f" {id[mid]:8} {lastName[mid]:10} {firstName[mid]:9} {class1[mid]:9} {class2[mid]:9} {class3[mid]:9}")
            print("---" * 50)
    
        else:
            print(f"Your search for {search} was not found") 
    
    elif search == "4": 
        search = input("Enter the class name you're looking for: ").upper() 

        for i in range(len(class1)): 
            for j in range(len(class1) - 1): 
                    if class1[j] > class1 [j + 1 ]: 

                        #swap places! for every value 
                        swap(j,id) 
                        swap(j, lastName) 
                        swap(j, firstName) 
                        swap(j, class1) 
                        swap(j, class2) 
                        swap(j, class3) 
        found_class = [] 

        for i in range(len(class1)): 
            if search.upper() in class1[i].upper():
                found_class.append(i)
        for i in range(len(class2)): 
            if search.upper() in class2[i].upper():
                found_class.append(i)
        for i in range(len(class3)): 
            if search.upper() in class3[i].upper():
                found_class.append(i)


        if not found_class:
            print(f"Your search for {search} was not found") 

        else: 
            print(f"{'ID':8} {'LNAME':10} {'FNAME':9} {'CLASS1':9} {'CLASS2':9} {'CLASS3':9}")
            print("---" * 50)
            for i in range(len(found_class)):
                print(f" {id[found_class[i]]:8} {lastName[found_class[i]]:10} {firstName[found_class[i]]:9} {class1[found_class[i]]:9} {class2[found_class[i]]:9} {class3[found_class[i]]:9}")
    elif search == "5":
        answer = "x"
        print("Thank you for using my program\nGoodbye:)")