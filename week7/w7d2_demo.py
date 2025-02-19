#W7D2 - Live Class: Review of Binary Search  & Binary search & Bubble + 2D Lists

def menu():
    print("Simple Searching Menu")
    print("1. Search by NAME")
    print("2. Search by NUM")
    print("3. Search by COLOR")
    print("4.EXIT")
    
    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1 ] = temp

import csv

#create your empty 1d parallel lists
names = []
nums = []
colors = []

valid_menu = ["1", "2", "3", "4"]
with open("week7/simple-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title())
#disconnected from file

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu:
        print("!INVALID ENTRY\nPlease try again\n")

    elif choice == "1": #search by NAME
        print('\nSearch by NAME')
        
        #bubble SORT before you binary search
        for i in range(len(names)):
            for j in range(len(names) - 1):
                #see if "heavier value is in front of "smaller" value
                if names[j] > names [j + 1 ]:
                    #swap places! not just THIS value, but all ASSOCIATED values!
                    swap(j,colors)
                    swap(j, names)
                    swap(j, nums)
        
        min = 0                         #always starting value --> FIRST INDEX / lowest value in ascending ordered list 
        max = len(names) - 1            #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) / 2)      #MIDDLE INDEX / middle value in ascending ordered list
    
        search = input("Enter the NAME you are looking for? ")

        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max) / 2)
        
        if search.lower() == names[mid].lower():
            print(f"Your search for {search} is complete, see below details: ")
            print(f"{'NAME':8}  {'NUM':3}  {'COLOR'}")
            print("-----------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}  {colors[mid]}")
            print("-----------------------------------------------")
        else:
            print(f"Your search for {search} was complete, and no information was found. ")

    elif choice == "2": #search by NUMBERS
        print("\nSearch by NUM")
        found = "x"
        print("\nSearch by NUM ")
        search = input("Enter the number you would like to search: ")
        
        for i in range(0, len(nums)):
            if search == nums[i]:
                found = i
            
        if found != "x":
            print(f"Your search for {search} is complete, see below details: ")
            print(f"{'NAME':8}  {'NUM':3}  {'COLOR'}")
            print("-----------------------------------------------")
            print(f"{names[i]:8}  {nums[i]:3}  {colors[i]}")
            print("-----------------------------------------------")
        else:
            print(f"Your search for {search} was complete, and no information was found. ")

    
    elif choice == "3": #search by COLOR
        print("\nSearch by COLOR")
        
        #bubble sort before you binary search!
        for i in range(len(colors)):
            for j in range(len(colors) - 1):
                #see if "heavier value is in front of "smaller" value
                if colors[j] > colors [j + 1 ]:
                    #swap places! not just THIS value, but all ASSOCIATED values!
                    swap(j,colors)
                    swap(j, names)
                    swap(j, nums)
        min = 0                         #always starting value --> FIRST INDEX / lowest value in ascending ordered list 
        max = len(colors) - 1           #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) / 2)      #MIDDLE INDEX / middle value in ascending ordered list
    
        search = input("Enter the COLOR you are looking for? ")

        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max)/ 2)
        
        if search.lower() == colors[mid].lower():
            print(f"Your search for {search} is complete, see below details: ")
            print(f"{'NAME':8}  {'NUM':3}  {'COLOR'}")
            print("-----------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}  {colors[mid]}")
            print("-----------------------------------------------")
        else:
            print(f"Your search for {search} was complete, and no information was found. ")

    
    else:
        print("\nEXIT")
        ans = "X" #ans changes from "y" to end the loop (condition will not eval as false)

print("\nThank you for using my program.\n\t\tGOODBYE!\n")

#-------- 2D LISTS ---------------------------------------------------

dataFile = [
    #this will be a 2D list to hold all of the file data
    names, # a list of names
    nums,   
    colors,
]
'''
with open("week7/simple-2.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        dataFile.append(rec)

'''
print("\n\nDATA FILE (2D LISTS[][]):")
for i in range(0,len(dataFile)):
    #accessing each list within the 2D list
    print(f"INDEX {i} of 'DataFile': {dataFile} ")
    for j in range(0,len(dataFile[i])):
        #accesssing each value within the list currently looked at from outter loop
        print(f"INDEX {i} and value DataFile[{j}]: {dataFile[i][j]}")