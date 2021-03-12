# This program prints and counts how many unique words are in the romeo.txt file
txt = "c:/Users/TechFast Australia/Dropbox/Programming/Python/List Exercises/romeo.txt"
uniqueWords = [] # List created to store unique words
f = open(txt, "r")
for x in f: # Loop through romeo.txt
    splitWords = x.split() # Split each word in romeo.txt
    for y in splitWords: # Loop created to check each word
        if y not in uniqueWords: # Check if word is not in list
            uniqueWords.append(y) # If the word isn't in the list it gets added
print("There are " + str(len(uniqueWords)) + " unique words used in this file.")
print(uniqueWords)
f.close()