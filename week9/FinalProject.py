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

def display(x, foundList, records):
    print(f"{'COMPANY':16}  {'TITLE':30}  {'AUTHOR':6}")
    print("----------------------------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{companys[x]:16}  {titles[x]:30}  {years[x]:6}")

    elif foundList:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{LibNums[foundList[i]]:7}  {titles[foundList[i]]:35}  {authors[foundList[i]]:17}  {genres[foundList[i]]:17} {pages[foundList[i]]:8} {status[foundList[i]]:11}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{LibNums[i]:7}  {titles[i]:35}  {authors[i]:18}  {genres[i]:17} {pages[i]:8} {status[i]:11}")
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
    print("Welcome to Red Box!\n")

    search = input("Enter what you would like to search: ")

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


    
        

