#Yarielis Diaz Colon 
#SE1116.02
#W1D2 Lab 1 
#1-7-2025 

#Program Prompt - A program that will determine if a meeting one is to full, if the number of peole is less than o

#Variable Dictionary 
#people -  the amount of people attending the room
#max_cap - the amount people allowed in the rom 

#Imports

#Functions
def difference(people, max_cap):
    '''Determines the number of people attending the meeting as wellas the the room capacity and return the difference. '''
    diff = people - max_cap
    print()
    return diff



#main code below ----------------------------------------------------------------------------------

meeting_name = input("What is the name of your meeting? ")
people = int(input("How many people are attending? "))
max_cap = int(input("What is the room capacity? "))

difference(people, max_cap)