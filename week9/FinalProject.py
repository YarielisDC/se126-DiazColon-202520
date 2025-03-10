#Yarielis Diaz Colon 
#SE116.02
#W9D2 Final Project
#3-4-2025

#--- imports ----
import csv
#--------------
#Empty List
companys = []
titles = []
years = []


#Functions
def swap(index,listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1 ] = temp
 

def menu():
    print("1. Show ALL")
    print("2. Search by COMPANYS")
    print("3. Search by TITLE")
    print("4. Search by YEAR")
    print("5. EXIT")
 
#Empty List
companys = []
titles = []
years = []

#Within the file
with open("week9/FinalProject.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        companys.append(rec[0])
        titles.append(rec[1])
        years.append(rec[2])

answer = "y"

while answer == "y":
    print("\nWelcome to Red Box!\n\n")
    menu()
    search = input("Enter what you would like to search: ").lower()

    if search not in ["1", "2", "3","4","5"]:
        print("***INVALID ENTRY!***\nPlease try again")
    
    elif search == "1":
        print("You have selected menu option 1:\nShow all movie titles")
        for i in range(len(companys)):
            for j in range(len(companys) - 1):
                if companys[j] > companys [j + 1 ]:
                    #swap places! for every value
                    swap(j,companys)
                    swap(j, titles)
                    swap(j, years)
 

            
        print(f"Your search for {search} was found! ")
        print(f"{'COMPANY':20} {'TITLE':26} {'YEAR':7}")
        print("---" * 50)
            
        for i in range(len(companys)):
            print(f"{companys[i]:20} {titles[i]:35} {years[i]:7}")
        print("---" * 50)
        
        
     
    if search == "2":
        print("You have selected option 2:\nSearch by company")
        #Making sure all the companies name are sorted before we look for them. 
            
        for i in range(len(companys)):
            for j in range(len(companys) - 1):
                if companys[j] > companys [j + 1 ]:
                    #swap places for every value
                    swap(j,companys)
                    swap(j, titles)
                    swap(j, years)
            
        search = input("Please enter the company you are searching for: ").lower()

        min = 0                         #always starting value --> FIRST INDEX / lowest value in ascending ordered list 
        max = len(companys) - 1         #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) / 2)      #MIDDLE INDEX / middle value in ascending ordered list


        while min < max and search.lower() != companys[mid].lower():
            if search.lower() < companys[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max)/ 2)

        found = []
        for i in range(len(companys)):
            if search.lower() in companys[i].lower():
                found.append(i)
            
        if not found:
            print(f"Your search for {search} was not found")
            
        else:
            print(f"{'COMPANY':20} {'TITLE':35} {'YEAR':7}")
            print( "---" * 50)
    
            for i in range(0,len(found)):
                print(f"{companys[found[i]]:20} {titles[found[i]]:35} {years[found[i]]}")
            print("---" * 50)
   
    if search == "3":
        print("You have selected option 3:\nSearch by title")
        #Making sure all the companies name are sorted before we look for them. 
        
        for i in range(len(titles)):
            for j in range(len(titles) - 1):
                if titles[j] > titles [j + 1 ]:
                    #swap places! for every value
                    swap(j,companys)
                    swap(j, titles)
                    swap(j, years)        
        min = 0 
        max = len(titles) - 1
        mid = int((min + max) / 2)

        while min < max and search.lower() != titles[mid].lower():
            if search.lower() < titles[mid].lower():
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1
            mid = int((min + max) / 2)  
        
        search = input("Enter the title you are looking for: ")
        found = []
        for i in range(len(titles)):
            if search.lower() in titles[i].lower():
                found.append(i)
            
        if not found:
            print(f"Your search for {search} was not found")
            
        else:
            print(f"{'COMPANY':20} {'TITLE':26} {'YEAR':7}")
            print( "---" * 50)
    
            for i in range(0,len(found)):
                print(f"{companys[found[i]]:20} {titles[found[i]]:35} {years[found[i]]:7}")
            print("---" * 50)
    if search == "4":
        print("You have selected option 4:\nSearch by Year")
        min = 0                         
        max = len(years) - 1         
        mid = int((min + max) / 2)      

        search = input("Enter the year you are looking for: ")
        while min < max and search.lower() != years[mid].lower():
            if search.lower() < years[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max)/ 2)
            
        found = []
        for i in range(len(years)):
            if search.lower() in years[i].lower():
                found.append(i)
            
        if not found:
            print(f"Your search for {search} was not found")
            
        else:
            print(f"{'COMPANY':20} {'TITLE':26} {'YEAR':7}")
            print( "---" * 50)
    
            for i in range(0,len(found)):
                print(f"{companys[found[i]]:20} {titles[found[i]]:35} {years[found[i]]}")
   
    
    if search == "5":
        answer = "x"
        print("Thank you for using our program\nGoodbye! ")

    
        

