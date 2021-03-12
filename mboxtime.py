# This program works out which hour of the day the most emails were received in mbox.txt
txt = "c:/Users/TechFast Australia/Dropbox/Programming/Python/List Exercises/mbox.txt"
hoursCount = dict() # Dictionary created to contain the hour and how many times it appears in mbox.txt
f = open(txt, "r")
for line in f: # Loop through mbox.txt
    if line.startswith("From "): # Only checking the lines that start with "From "
        hoursplit = line.split()[5] # Splitting the string at index 5 to get the timestamp
        hours = hoursplit.split(":")[0] # Splitting the string again at index 0 and cutting it off before the colon
        if hours in hoursCount: # If/else statement to check if the hour appears in the dictionary. If it appears, the value increments by 1, if not the key is added and is given the value of 1
            hoursCount[hours] += 1
        else:
            hoursCount[hours] = 1
lst = list() # List created to store dictionary items so they can be sorted by keys in numerical order
for key, val in list(hoursCount.items()):
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)