# Name: Yarielis Diaz Colon
# Lab: 6 Week 9
# Date: December 4, 2024
# Course Name: SE-116.02

# PROGRAM PROMPT:    1. Number of individuals not eligible to register.
#                   2. Number of individuals who are old enough to vote but have not registered.
#                   3. Number of individuals who are eligible to vote but did not vote.
#                   4. Number of individuals who did vote.
#                   5. Number of records processed.

# ---------------------------------------------------------------------------------------------------------------
# IMPORTS
from os import system, name


# FUNCTIONS
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def increment_counter(counter):
    return counter + 1


def more():
    ans = input("Would you like to go again? [y/n]: ").upper()
    
    while ans != 'Y' and ans != "N":
        print("Please enter 'Y' or 'N'.")
        ans = input("Would you like to go again? [y/n]: ").upper()
    return ans


# ---------------------------------------------------------------------------------------------------
# MAIN CODE BELOW

clear()


records_processed = 0  # Total records processed

ans = "Y"

while ans    == "Y":
    id = input("Welcome! Can I have your ID number: ")
    age = int(input("What is your age? "))

    # Increment the records processed
    records_processed = increment_counter(records_processed)

    # Check if the person is not eligible to register (under 18)
    if age < 18:
        print("You're unable to register because you're not over 18.")
        print(f"\n\t| ID: {id} | Age: {age} | Registered to Vote: N | Voted: N |")
      
    
    else:
        # Check if they are registered to vote
        register = input("You are over the age of 18 but are you registered to vote [Y/N]? ").upper()

        if register == "Y":
            vote = input("Great! You've met all the criteria to vote. Would you like to cast a vote [y/n]? ").upper()
            
            # If they voted
            if vote == "Y":
                print(f"\n\t| ID: {id} | Age: {age} | Registered to Vote: Y | Voted: Y |")
               

            elif vote == "N":
                print(f"You're vote was not inputted.")
                print(f"| ID: {id} | Age: {age} | Registered to Vote: Y | Voted: N |")
              

        elif register == "N":
            print("You're unable to vote because you're not registered.")
            print(f"\n\t| ID: {id} | Age: {age} | Registered to Vote: N | Voted: N |")
            

    # Ask the user if they want to continue and see records processed
        ans = more()
        Number_P = input("Would you like to see the records processed [y/n]: ")
        
        if Number_P == "y": 
            print(f"Total number of records processed: {records_processed}")
            print("Thanks for using my program. ")
 