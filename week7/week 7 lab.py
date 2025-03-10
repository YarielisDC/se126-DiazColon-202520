#Yarielis Diaz Colon 
#SE116.02
#W7D2 Lab 7
#2-26-2025 

#Program Prompt: Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and
#the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a 
#user to interact with the dictionary based on the following menu

# -- imports
import csv
#---------

# -- lists ---
library = {
"python" : "a popular programming language created by Guido van Rossum",
"documentation" : "programming comments; notes within code which explain what the code does",
"flowchart" : "a visualization of how a computer program's instructions are read",
"variable" : "a friendly name that has data stored or assigned to it inside of a computer program",
"assignment" : "the process of storing a data value to a friendly name in programming",
"output" : "data displayed out of a computer program",
"input" : "data taken into a computer program - usually entered by a user or read from a text file",
"string" :"a data type which holds all characters (alpha/special/numeric)",
"integer" : "a data type which holds whole numbers (no decimals!)",
"float" : "a data type which holds numbers (including decimals!)",
"boolean" : "a data type which means either 'true' or 'false",
"condition" : "a programming statement which allows the execution or skip of a block of code based on its evaluation (either 'true' or 'false')",
"loop" : "a repetition sequence - a block of code that can be executed multiple times in succession based on the evaluation of its condition",
"if" : "a single-decision statement - a block of code that can be executed or skipped based on the evaluation of its condition",
"else" : "a single-decision statement which executes when its paired and preceding 'if statement' evaluates as false",
"while" : "a type of loop which repeats an unknown number of times (based on a stored value)",
"for" : "a type of loop which repeats a set number of times",
"function" : "a sequence of code which performs a specific task whenever called",
"argument" : "a value passed to a function to fulfill a parameter",
"parameter" : "a variable created in a function definition header which is initialized when an argument is passed into the function",
"list" :" a Python collection type which stores multiple items/values to a name and whose values are accessed by referencing the name and index (location) of said value",
"dictionary" :"a Python collection type which stores multiple items/values to a name and whose values are acceessed by referencing the string index of the value",
"csv" : "comma separated value files - commonly used as data files in programming",
"index" : "a key for list and dictionary collection types - integer based for standard lists and string based for dictionaries",
"key" : "a string index or property name which has data associated to it in a dictionary",
}
    
#functions
def menu():
    '''Showing menu options through 1-4'''
    print("The Menu")
    print("1. Show for a word")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. Exit")
#--------

#within the file
with open ("week7/words.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        library.update({rec[0] : rec[1]})

#MAIN EXECUTING CODE
ans = "y"
while ans== "y":
   
    #showing menu options  
    menu()

    search = input("Please select a number [1-4] ")

    if search  == "1":
        print("You have chosen to select ")