#Yarielis Diaz Colon 
#SE1116.02
#W4D2 Lab 4
#1-28-2025 

#PROGRAM PROMPT: This is a two-part program where you will work on creating and populating parallel lists based on file data, then create
#and write data to a file.

    #PART 1: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in
    #the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique
    #email address, a department, and a unique phone extension.

    #PART 2: Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the
    #same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last
    #name, email, department, and phone extension. #Note: each employee’s data should be on its own record (row) within
    #he newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab
    #as we will not be reprocessing the data found in this new file)

#------------------ Imports -------------------------------
import csv

#----------------- WITHIN the file -----------------------

#Known Variable
answer = "y"
#Known Lists 
firstN = []
lastN = []
age = []
screenN = []
house_a = []
rd_count = []
m_count = []
hr = []
acc = []
sale = []
aud = []
with open ("week4/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file: 
    #Assigning field data to the Lists
     firstN.append(rec[0])
     lastN.append(rec[1])
     age.append(rec[2])
     screenN.append(rec[3])
     house_a.append(rec[4])
#-------------- disconnected from the file --------------------------

#EMAIL.
email = []
for i in range(0, len(screenN)):
    e = (screenN[i] + "@westeros.net")
    email.append(e)

#Department
department = []
for i in range(0, len(house_a)):
    
    if house_a[i] in "House Stark":
        d = "Research & Development"
        department.append(d)
        c = 0 + 1
        rd_count.append(c)

    
    elif house_a[i] in "House Targaryen":
        d = "Marketing"
        department.append(d)
        m = 0 + 1
        m_count.append(m)
    
    elif house_a[i] in "House Tully":
        d = "Human Resources"
        department.append(d)
        h = 0 + 1 
        hr.append(h)
    
    elif house_a[i] in "House Lannister":
       d = "Accounting" 
       department.append(d)
       a = 0 + 1
       acc.append(a)

    elif house_a[i] in "House Baratheon":
       d = "Sales"
       department.append(d)
       s = 0 + 1 
       sale.append(s)

    elif house_a[i] in "The Night's Watch":
       d = "Auditing"
       department.append(d)
       au = 0 + 1 
       aud.append(au)

    #Phone Extension
phone = []
for i in range(0, len(department)):
        if department[i] in "Research & Development":
          pe = "100 - 199"
          phone.append(pe)
       
        elif department[i] in "Marketing":
          pe = "200 - 299"
          phone.append(pe)
       
        elif department[i] in "Human Resources":
          pe = "300 - 399"
          phone.append(pe)
        
        elif department[i] in "Accounting":
          pe = "400 - 499"
          phone.append(pe)
        
        elif department[i] in "Sales":
           pe = "500 - 599"
           phone.append(pe)
        
        elif department[i] in "Auditing":
           pe = "600 - 699"
           phone.append(pe)

#Display
print(f'{"FIRST":8} {"LAST":10} {"EMAIL":30} {"DEPARTMENT":23}  {"PHONE EXTEN.":11}')

for i in range(0, len(firstN)):
    print(f"{firstN[i]:8} {lastN[i]:10} {email[i]:30} {department[i]:23} {phone[i]:11}")

print(f"\nThere are {len(firstN)} employees total")
print(f'There are {len(rd_count)} in the Research & Development Department')
print(f'There are {len(m_count)} in the Marketing Department')
print(f'There are {len(hr)} in the Human Resources')
print(f'There are {len(acc)} in the Accounting')
print(f'There are {len(sale)} in the Sales')
print(f'There are {len(aud)} in the Auditing\t')


#creating a new CSV file:
file = open('week4/westeros.csv', "w")
for i in range(0, len(firstN)):
   file.write(f'{firstN[i]}, {lastN[i]}, {email[i]}, {department[i]}, {phone[i]}\n')
   file.close


while answer == "y":
    print(f"\nWesteros Services Directory Search\n\t")
    print("1. Search by FIRST NAME")
    print("2. Search by LAST NAME")
    print("3. Search By DEPARTMENT")
    print("4. Search by PHONE EXETENSION")
    print("5. EXIT")
    found = "x"
    search = input("What would you like to search by? ")

    #Searching by first names
    if search == "1":
        print("\nSearching by FIRST NAME:")
        firstnS = input("What is the FIRST NAME you would like to search: ")

        for i in range(0, len(firstN)):
            if firstnS in firstN[i]:
                found = i
    
        if found != "x":
            print(f"\tYour search for {firstnS} was found\t\t")
            print(f'{"FIRST":8} {"LAST":10} {"EMAIL":30} {"DEPARTMENT":23}  {"PHONE EXTEN.":11}')
            print(f"{firstN[found]:8} {lastN[found]:10} {email[found]:30} {department[found]:23} {phone[found]:11}")
            
        else:
            print(f"Your search for {firstnS} was NOT Found")

    elif search == "2":
        print("Search by LAST NAME")
        found = []
        LastNs = input("\n\tWhat is the LAST NAME you would like to search: ")

        for i in range(0, len(lastN)):
            if LastNs in lastN[i]:
                found.append(i)
        
        if found != "x":
            print(f"Your search for {LastNs} was found!")
            print(f'\n{"FIRST":8} {"LAST":10} {"EMAIL":30} {"DEPARTMENT":23}  {"PHONE EXTEN.":11}')
            for i in range(0, len(found)):
                print(f"{firstN[found[i]]:8} {lastN[found[i]]:10} {email[found[i]]:30} {department[found[i]]:23} {phone[found[i]]:11}")
        
        else:
            print(f"Your search for {LastNs} was NOT Found")

    elif search == "3":
        print("Search by DEPARTMENT")
        found = []
        depS = input("What is the department you would like to search for? ")
    
        for i in range(0,len(department)):
            if depS in department[i]:
                    found.append(i)

        if found != "x":
            print(f"Your search for {depS} was found!")
            print(f'\n{"FIRST":8} {"LAST":10} {"EMAIL":30} {"DEPARTMENT":23}  {"PHONE EXTEN.":11}')
            for i in range(0,len(found)):
                    print(f"{firstN[found[i]]:8} {lastN[found[i]]:10} {email[found[i]]:30} {department[found[i]]:23} {phone[found[i]]:11}")
        else:
                print(f"Your search for {depS} was not found!")
        
    elif search == "4":
        found = []
        print("Search by Phone Exetension")
        pe_s = input("Enter the phone exetensions you're looking for: ")

        for i in range(0,len(phone)):
            if pe_s in phone[i]:
                found.append(i)
        
        if found != "x":
            print(f"Your search for {pe_s} was found!")
            print(f'\n{"FIRST":8} {"LAST":10} {"EMAIL":30} {"DEPARTMENT":23}  {"PHONE EXTEN.":11}')
            
            for i in range(0,len(found)):
                print(f"{firstN[found[i]]:8} {lastN[found[i]]:10} {email[found[i]]:30} {department[found[i]]:23} {phone[found[i]]:11}")
            
        else: 
            print(f"Your search for {pe_s} was not found!")


    
    elif search == "5":
        print("EXIT")
        answer == "o"
        print("Goodbye!")
    
    answer = input("Would you like to use the search again: ")
    
    
    




