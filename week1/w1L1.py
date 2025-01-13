#Yarielis Diaz Colon 
#SE1116.02
#W1D2 Lab 1 
#1-7-2025 

#Program Prompt - A program that will determine if a meeting room is to full, if the number of peole is less than o

#Variable Dictionary 
#people -  the amount of people attending the room
#max_cap - the amount people allowed in the rom 
#response - User's response if they would like to continue or not 
#Imports

#Functions
def difference(people, max_cap):
    '''Determines the number of people attending the meeting as well as  the room capacity and return the difference. '''
    diff = people - max_cap
    print()
    return diff
def decision(response):
    '''The Users's respoonse to whether or not they would like to continue in the program and enter another meeting's information'''
    while response != 'y' and response != 'n':
        respopnse = input("Invalid input. Please enter'y' for yes or 'n' for no").lower()
    return response




#main code below ----------------------------------------------------------------------------------

meeting_name = input("What is the name of your meeting? ")
people = int(input("How many people are attending? "))
max_cap = int(input("What is the room capacity? "))

difference(people, max_cap)

response = input("Would you like to continue? 'y' for yes 'n' for no: ").lower()
