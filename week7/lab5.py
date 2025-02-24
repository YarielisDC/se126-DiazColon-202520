#Yarielis Diaz Colon 
#SE1116.02
#W6D2 Lab 5
#2-11-2025 

#PROGRAM PROMPT: MAKING A MENU BASED PROGRAM:
#Personal Library Menu
#1. Show All Titles – list all book data to the user alphabetically by title
#2. Search by Title – allow for an entire title or a title key word
#3. Search by Author – show all titles of the searched-for author
#4. Search by Genre - show all titles of the searched-for genre
#5. Search by Library Number – only allow for one specific library number item
#6. Show All Available – show all titles with status “available”
#7. Show All On Loan - show all titles with status “on loan”
#8. EXIT
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,
#Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches

#csv file used: booklist.csv

#---------- IMPORTS --------------------
import csv 
#---------- FUNCTION ------------------
def display(x, foundList, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple
                when x != "x" it is an index and we have one value, otherwise we have multiple

            records   the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'LIB NUM':7}  {'TITLE':35}  {'AUTHOR':18}  {'GENRE':17} {'PAGES':8} {'STATUS':11}")
    print("-----------------------------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{LibNums[x]:7}  {titles[x]:35}  {authors[x]:18}  {genres[x]:17} {pages[x]:8} {status[x]:11}")

    elif foundList:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{LibNums[foundList[i]]:7}  {titles[foundList[i]]:35}  {authors[foundList[i]]:17}  {genres[foundList[i]]:17} {pages[foundList[i]]:8} {status[foundList[i]]:11}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{LibNums[i]:7}  {titles[i]:35}  {authors[i]:18}  {genres[i]:17} {pages[i]:8} {status[i]:11}")
def menu():
    print("\nWelcome to the Libray Search System")
    print("Please look through 1-8 options to search for\n")
    print("1. Show all Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Search by Avaliable Books")
    print("7. Show Books Currently in a Loan")
    print("8. EXIT")

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1 ] = temp

#--------- KNWON VARIABLES -----------------------
ans = "y"
#--------- LISTS -----------------------
LibNums = []
titles = []
authors = []
genres = []
pages = []
status = []

#-------- WITHIN CSV FILE -------------------
with open ("week7/book_list.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        LibNums.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])
        status.append(rec[5])
#disconnected from file


while ans == "y":
    menu()
    search = input("Enter what you would like to search: ")

    if search not in ["1", "2", "3","4","5","6","7","8",]:
        print("***INVALID ENTRY!***\nPlease try again")

    elif search == "1":
        print("Show all Book Titles")
        for i in range(len(titles)):
            for j in range(len(titles) - 1):
                #see if "heavier value is in front of "smaller" value
                if titles[j] > titles [j + 1 ]:
                    #swap places! not just THIS value, but all ASSOCIATED values!
                    swap(j,titles)
                    swap(j, authors)
                    swap(j, genres)
                    swap(j, LibNums)
                    swap(j, pages)
                    swap(j, status)
        display("x", 0, len(titles))
        min = 0 
        max = len(titles) - 1
        mid = int((min + max) / 2)

        while min < max and search != titles[mid]:
            if search < titles[mid]:
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1
            
            mid = int((min + max) / 2)  

        if search == titles[mid]:
            display(mid, 0, len(titles))
    
    elif search == "2":
        for i in range(len(titles)):
            for j in range(len(titles) - 1):
                #see if "heavier value is in front of "smaller" value
                if authors[j] > authors [j + 1 ]:
                    #swap places! not just THIS value, but all ASSOCIATED values!
                    swap(j,titles)
                    swap(j, authors)
                    swap(j, genres)
                    swap(j, LibNums)
                    swap(j, pages)
                    swap(j, status)
        
        search = input("Please Enter the title you are looking for? ").lower()  
        min = 0                         #always starting value --> FIRST INDEX / lowest value in ascending ordered list 
        max = len(authors) - 1           #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) / 2)      #MIDDLE INDEX / middle value in ascending ordered list


        while min < max and search.lower() != titles[mid].lower():
            if search.lower() < titles[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max)/ 2)

        found = []

        for i in range(0,len(titles)):
            if search.lower() in titles[i].lower():
                found.append(i)

        if not found:
            print(f"Your search for {search} was not found!")
        else:
            display("x",found,len(found))
    
    elif search == "3":
        for i in range(len(authors)):
            for j in range(len(authors) - 1):
                #see if "heavier value is in front of "smaller" value
                if authors[j] > authors [j + 1 ]:
                    #swap places! not just THIS value, but all ASSOCIATED values!
                    swap(j,titles)
                    swap(j, authors)
                    swap(j, genres)
                    swap(j, LibNums)
                    swap(j, pages)
                    swap(j, status)
        search = input("Please Enter the Author you are looking for? ").lower()  
        min = 0                         #always starting value --> FIRST INDEX / lowest value in ascending ordered list 
        max = len(authors) - 1           #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) / 2)      #MIDDLE INDEX / middle value in ascending ordered list


        while min < max and search.lower() != authors[mid].lower():
            if search.lower() < authors[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max)/ 2)

        found = []

        for i in range(0,len(authors)):
            if search.lower() in authors[i].lower():
                found.append(i)

        if not found:
            print(f"Your search for {search} was not found!")
        else:
            display("x",found,len(found))

    elif search == "4":
        print(f"\nYou have chosen to search by Genre")
        search = input("Which genre are you lookin for: ").lower()
        found = []

        for i in range(0,len(genres)):
            if search.lower() in genres[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, we hae no genre related to the meaning you entered: '{genres}'")
        else:
            display("x",found,len(found))

    elif search == "5":
        print("You have chosen to search by Library Numbers")
        search = input("Please Enter the Library number: ")
        found = "x"
       
        for i in range(0,len(LibNums)):
            if search.lower() in LibNums[i].lower():
                found = i
        #step 3: filter and display results
        if found != "x": #search was found!
            print(f"Your search for {search} was found ")
            print(f"{'LIB NUM':7}  {'TITLE':35}  {'AUTHOR':18}  {'GENRE':17} {'PAGES':8} {'STATUS':11}")
            print("-----------------------------------------------------------------------------------------------------------------")
            print(f"{LibNums[found]:7}  {titles[found]:35}  {authors[found]:18}  {genres[found]:17} {pages[found]:8} {status[found]:11}")
        
        else:
            print(f"Your search for {search} was not  found ")
            
    elif search == "6":
        print(f"\nYou have chosen to search through all AVALIABLE BOOKS")

        found = []

        # Step 1: Find books with status "available"
        for i in range(len(status)):
            if status[i].lower() == "available":
                found.append(i)

        # Step 2: Display results
        if not found:
            print("Your search didn't come up.")
        else:
            print("\nAvailable Books:")
            print(f"{'LIB NUM':7}  {'TITLE':35}  {'AUTHOR':18}  {'GENRE':17} {'PAGES':5} {'STATUS':11}")
            print("-----------------------------------------------------------------------------------------------------------------")
            for i in found:
                print(f"{LibNums[i]:7}  {titles[i]:35}  {authors[i]:18}  {genres[i]:17} {pages[i]:8} {status[i]:11}")

    elif search == "7":
        print(f"\nYou have chosen to search through all UNAVALIABLE BOOKS")

        found = []

        # Step 1: Find books with status "available"
        for i in range(len(status)):
            if status[i].lower() == "on loan":
                found.append(i)

        # Step 2: Display results
        if not found:
            print("Your search didn't come up.")
        else:
            print("\nUnavailable Books:")
            print(f"{'LIB NUM':7}  {'TITLE':35}  {'AUTHOR':18}  {'GENRE':17} {'PAGES':5} {'STATUS':11}")
            print("-----------------------------------------------------------------------------------------------------------------")
            for i in found:
                print(f"{LibNums[i]:7}  {titles[i]:35}  {authors[i]:18}  {genres[i]:17} {pages[i]:8} {status[i]:11}")

    elif search == "8":
        ans = "x"
        print("Thank you for using my Libray search program!\nGoodbye!")