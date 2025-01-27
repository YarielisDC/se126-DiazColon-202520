#Yarielis Diaz Colon 
#SE1116.02
#W3D2 Lab 3
#1-26-2025 

#Prompt: 
#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.

#Variable Dictionary-----------------------------------------------------------------------------
cant_register = 0    #1
haven_registered = 0 #2
didn_vote = 0        #3
did_vote = 0         #4 
total_rec = 0        #5
#------------------------------------------------------------------

#---------------Import------------------------
import csv  

#---------------LISTS--------------------------------------------------
id = []
age = []
register = []
vote = []

#----------------------------------------



#IN CSV FILE
with open("week3/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    

    for rec in file:

        id.append(rec[0])
        age.append(rec[1])
        register.append(rec[2])
        vote.append(vote[3])

        #NOT OLD ENOUGH TO VOTE!
        if rec[1] <= "17":
            cant_register += 1
        
        #PEOPLE WHO ARE OF AGE BUT DIDN'T REGISTER!
        if rec[1] >= "18":
                if rec[2] == "N":
                    haven_registered += 1
        
        #PEOPLE WHO ARE OF AGE, DID REGISTER BUT DIDN'T VOTE!
        if rec[1] >= "18":
             if rec[2] == "Y":
                  if rec[3] == "N":
                       didn_vote += 1
        #PEOPLE WHO ARE OF AGE, DID REGISTER AND DID VOTE!              
        if rec[3] == "Y":
             did_vote += 1

        if rec[0] >= "1":
             total_rec += 1
            

              
        
        
print(f"Number of individuals not eligible to register: {cant_register} ")
print(f"Number of individuals who are old enough to vote but have not registered: {haven_registered}")
print(f"Number of individuals who are eligible to vote but did not vote: {didn_vote}")
print(f"Number of individuals who did vote: {did_vote}")
print(f"Number of records processed: {total_rec}")

    