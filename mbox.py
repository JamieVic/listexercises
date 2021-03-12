# This program checks the mbox.txt file for the most emails received from, the most popular email domain that appears and the most emails received in a weekday.
txt = "c:/Users/TechFast Australia/Dropbox/Programming/Python/List Exercises/mbox.txt"
# Dictionaries created to get the data (key) and the count (value)
emails = dict()
days = dict()
domains = dict()
f = open(txt, "r")
for line in f: # Loop through mbox.txt to collect data
    if line.startswith("From "): # Only checking lines that start with "From "
        # Strings are split to only get the data we need for the corresponding dictionaries
        emailaddress = line.split()[1]
        splitdomain = line.split()[1]
        domainname = splitdomain.split("@")[1]
        weekday = line.split()[2]
        # If/else statements check if the key has been added. If it has the value increments by 1, if not the key is added with a value of 1
        if emailaddress in emails:
            emails[emailaddress] += 1
        else:
            emails[emailaddress] = 1
        if domainname in domains:
            domains[domainname] += 1
        else:
            domains[domainname] = 1
        if weekday in days:
            days[weekday] += 1
        else:
            days[weekday] = 1
# Max functions work out which key and value have the highest number
maxEmails = max(emails, key = emails.get)
maxDomains = max(domains, key = domains.get)
maxDays = max(days, key = days.get)
print("The most emails came from " + maxEmails + " with " + str(emails[maxEmails]) + " emails, and the most emails received in a day was on " + maxDays + " with " + str(days[maxDays]) + " received. The domain with the most emails sent is from " + maxDomains + " with " + str(domains[maxDomains]) + " received.")
print(emails, domains, days)