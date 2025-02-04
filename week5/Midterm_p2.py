#Yarielis Diaz Colon
#SE.126
#2/4/25

#imports
import csv
#---------
#KNOWN VARIABLES
answer = "y"
#lists 

firstN = []
lastN = []
email = []
departmet = []
phone_exe = []


#OPENING CSV FILE
with open ("week5/westeros.csv") as csvfile:
    file = csv.reader(csvfile)
    #saving the data from file to the lists
    for rec in file:
        firstN.append(rec[0])
        lastN.append(rec[1])
        email.append(rec[2])
        departmet.append(rec[3])
        phone_exe.append(rec[4])


#MAKING A NEW LIST FOR OFFICE NUMBER
office_num = []



for i in range(0, len(firstN)):
    
    if firstN[i] == "Eddard":
        o = "101"
        office_num.append(o)
    elif firstN[i] == "Benjen":
        o = "102"
        office_num.append(o)
    elif firstN[i] == "Catelyn":
        o = "103"
        office_num.append(o)
    elif firstN[i] == "Arya":
        o = "103.5"
        office_num.append(o)
    elif firstN[i] == "Robb":
        o = "104"
        office_num.append(o)
    elif firstN[i] == "Sansa":
        o = "105"
        office_num.append(o)
    elif firstN[i] == "Bran":
        o = "106"
        office_num.append(o)
    
    elif firstN[i] == "Rickon":
        o = "107"
        office_num.append(o)
    elif firstN[i] == "Jon":
        o = "108"
        office_num.append(o)
    elif firstN[i] == "Tyrion":
        o = "109"
        office_num.append(o)
    elif firstN[i] == "Jaime":
        o = "110"
        office_num.append(o)
    elif firstN[i] =="Cersei":
        o = "111"
        office_num.append(o)
    elif "Robert" == firstN[i]:
        o = "112"
        office_num.append(o)
    elif firstN[i] == "Stannis":
        o = "113"
        office_num.append(o)
    elif firstN[i] == "Renly":
        o = "114"
        office_num.append(o)
    elif firstN[i] == "Daenerys":
        o = "115"
        office_num.append(o)
    elif firstN[i] == "Viserys":
        o = "116"
        office_num.append(o)


print(f"{"FirstName":20} {"Last Name":20} {"Email":30} {"Department":25} {"Phone Extension":30} {"Office Number"}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,len(office_num)):
    print(f"{firstN[i]:20} {lastN[i]:20} {email[i]:30} {departmet[i]:25} {phone_exe[i]:30} {office_num[i]}")


print(f'There are a total of {len(firstN)} employees')
    



#SEQUENTIAL SEARCH
while answer == "y":
    print("\n\tWesteros Services Directory Search")
    print("1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. EXIT")

    found = "x"
    search = input("What search type are you looking for: ")

    if search == "1":
        ems = input("What is the email you are looking for? ")
        
        for i in range(0,len(email)):
            if ems == email[i]:
                found = i
        
        if found != "x":
            print(f"Your search for {ems} was found!")
            print(f"{"FirstName":20} {"Last Name:":20} {"Email":30} {"Department":25} {"Phone Extension":30} {"Office Number"}")
            print(f"{firstN[found]:20} {lastN[found]:20} {email[found]:30} {departmet[found]:25} {phone_exe[found]:30} {office_num[found]:5}")
        else:
            print(f"Your search for {ems} was not found")

    if search == "2":
        found = []
        print("Search by DEPARTMENT")
        deps = input("What is the department you are looking for? ")

        for i in range(0,len(departmet)):
            if deps in departmet[i]:
                found.append(i)
        if not found:
            print(f"Your search for {deps} was not found!")

        else:
            print(f"Your search for {deps} was found")
            print(f"{"FirstName":20} {"Last Name:":20} {"Email":30} {"Department":25} {"Phone Extension":30} {"Office Number"}")
            for i in range(0,len(found)):
                print(f"{firstN[found[i]]:20} {lastN[found[i]]:20} {email[found[i]]:30} {departmet[found[i]]:25} {phone_exe[found[i]]:30} {office_num[found[i]]}")
        
    if search == "3":
        print("EXIT")
        answer = "n"
        print("Goodbye!")
    answer = input("Would you like to use the search again? ")


