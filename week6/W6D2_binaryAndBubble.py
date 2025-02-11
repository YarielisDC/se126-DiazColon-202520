#W6D2 - Binary Search + Bubble Sort

#this file uses party.csv

#programPrompt: Build a repeatable, menu- driven progream to access and search for data within the file

#--Imports ------------------------------------------------------------------------------------------------------------------------------
import csv


#--Functions ---------------------------------------------------------------------------------------------------
def display(x, foundlist,records):
        '''PARAMETERS:
               x signifier for if we are printing a single record or multiple when x != "x" we have one value otherwise we have multiple
                records the length of a list we are going to process through (3 of loops/prints) '''
        
        print(f"{'CLASS':8} {'NAME':10} {'MEANING':25} {'CULTURE'}")
        print("------------------------------------------------------")

        if x != "x":
             #printing one record
            print(f"{class_type[x]:8} {name[x]:10} {meaning[x]:25} {culture[x]}")
        elif foundlist:
            #printing multiples, based on length stored in 'foundlist'
            for i in range(0,records):
                print(f"{class_type[foundlist[i]]:8} {name[foundlist[i]]:10} {meaning[foundlist[i]]:25} {culture[foundlist[i]]}")
        else:
        #printing multiples, based on length stored in records
            for i in range(0,records):
                print(f"{class_type[i]:8} {name[i]:10} {meaning[i]:25} {culture[i]}")
        print("----------------------------------------------------------")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
#-- Main Executing Code ----------------------------------------------------------------------------------------
class_type = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

with open ("week6/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
# disconnected from file ---------------------------------------------------------------------------------------

#display whole list data to user
display("x",0,len(class_type)) #practice with function

ans = input("Would you like to enter the search program? [y/n] ").lower()

#validity and user errot trap loop
while ans != "y" and ans != "n":
        print("***INVALID ENTRY!***")
        ans = input("Would you like to enter the search program? [y/n] ").lower()

#main searching lop
while ans == "y":
    print("\tSearching Menu")
    print("1. Search by Type") #shows all of either elf or dragon
    print("2. Search by Name") #binary search review
    print("3. Search by Meaning") #find part of a while
    print("4. Exit")
    search_type = input("\nHow would you like to search today? [1-4]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4",]:
         print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":
        print(f"\nYou have chosen to search by TYPE")
        search = input("Which type: 'dragon' or 'elf': ").lower()
         
        if search not in ["dragon", "elf"]:
            #could also be: if search.title() not in class_type:
            print("***INVALID ENTRY!***\nPlease try again")
        
        else:
            found = []
            for i in range(0,len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)
            if not found:
                print(f"Sorry, your search for {search} could not be completed")
            else:
                print(f"Your seach for {search} is complete! Details below: ")
                display("x", found,len(found))
    elif search_type == "2":
        #BUBBLE SORT----------------------------------------

        for i in range(0, len(name) - 1):#outter loop
            for index in range(0, len(name) - 1):#inner loop

                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing

                if(name[index] > name[index + 1]):
                    #if above is true, swap places!
                    swap(index,name)
                #swap all other values
                    swap(index, class_type)
                    swap(index, meaning)
                    swap(index, culture)
        #check your sorting
        display("X",0,len(name))

        #Binary Search
        search = input("Enter the NAME you are looking for: ")
        min = 0
        max = len(name) - 1
        mid = int((min + max) / 2)

        while min < max and search_type != name[mid]:
            if search <name[mid]:
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1
            
            mid = int((min + max) / 2)

        if search == name[mid]:
            display(mid, 0, len(name))
        else:
            print(f"\nYour search for {search} came up empty")
    
    elif search_type == "3":
        print(f"\nYou have chosen to search by MEANING")
        search = input("Which name meaning are you lookin for: ").lower()

        found = []
    
        #allow the program to search for parts of a name like 'dragon' or 'light
        for i in range(0,len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, we hae no names related to the meaning you entered: '{meaning}'")
        else:
            display("x",found,len(found))
    
    elif search_type == "4":
        print(f"\nYou have chosen to EXIT")
        ans = "N"

        
 