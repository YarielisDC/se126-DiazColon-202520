#W6D1 - Searching Algorithms: Binary vs Sequential Search

import csv

library_num = []
title = []
authors = []
genres = []
pages = []

with open("week6\library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        library_num.append(rec[0])
        title.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'Lib#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {"PAGES":5}")
print("-------------------------------------------------------------------------------")

for i in range(0, len(library_num)):
    print(f"{library_num[i]:5} {title[i]:25} {authors[i]:15} {genres[i]:20} {pages[i]:5}")
print('---------------------------------------------------------------------------------')

#Sequential  Search: allow a user to search for a specific title
#titles is NOT ordered

found = []
seq_count = 0 
search_num = input("Which library number are you looking for? ")

for i in range(0, len(library_num)):
    seq_count += 1 
    if search_num in library_num[i]:
        found.append(i)

if not found:
        print(f"Sorry your search for {search_num} was not found")
    
else:
    print(f"Your search for {search_num} was found")
    print(f"{'Lib#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {"PAGES":5}")
    print("-------------------------------------------------------------------------------")
        
for i in range(0,len(found)):
    print(f"{library_num[found[i]]:5} {title[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5}")
    print("--------------------------------------------------------------------------------")

#BINARY SEARCH: must be performed on ORDERED lists (library_nums)

min = 0
max = len(library_num) - 1
mid = int((min + max) / 2)

bin_count = 0

while min < max and search_num != library_num[mid]:
    #min < max --> list has not been exhausted of potential values yet
    #search_num != library_nums[mid]--> what we are lookinf gor is not in the mid position

    if search_num < library_num[mid]:
        #everything after mid point is not possible
        max = mid - 1

    else:
        #everything before mid point is not possible
        min = mid + 1
    
    mid = int((min + max) / 2)
    bin_count += 1

print(f"BINARY SEARCH ITERATIONS: {bin_count}")

if search_num == library_num[mid]:
    print(f"Your search for {search_num} was found")
    print(f"{'Lib#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {"PAGES":5}")
    print("-------------------------------------------------------------------------------")
    print(f"{library_num[mid]:5} {title[mid]:25} {authors[mid]:15} {genres[mid]:20} {pages[mid]:5}")
    print("-------------------------------------------------------------------------------")

else:
    print(f"Sorry, your search for {search_num} was not found")