#Name Yarielis Diaz Colon
#Lab: W4D2 In Class lab
#Date: 10/22/24
#Course Name: SE116.02

#Program Prompt: 

#Assigning named Variables
tax = 20/100
employee_count = 0 


answer = "y"
while answer == "y" or answer == "Y":
#---------------------------------------------------------------------- Below is in a loop -------------------------------------------------------------------------------------
    name = (input("Enter your employee's name: "))
    rate = float(input("Enter your hourly rate: $"))
    hours = float(input("Enter your hours in a week: "))
    weeks = int(input("How many weeks are you being paid for? "))
    

    gross = rate * hours * weeks
    taxAmt = gross * tax
    net = gross - taxAmt

    #update count & totals: employee_count, total_gross, total_tax, total_net
    employee_count = employee_count + 1 
    print(f"Employee:               {name}")
    print(f" Gross Pay: ${gross:10.2f}")
    print(f"Taxes Paid: ${taxAmt:10.2f}")
    print(f"   Net Pay: ${net:10.2f}")
   
    #BUILT A WAY OUT
    answer = input("\nWould you like to enter another employee? [y/n]: ")