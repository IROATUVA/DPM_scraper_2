#This is a program wholly devoted to looking at the IRO Venmo and collecting information about who has and has not paid dues
#Developed by Mohit Srivastav - IRO Treasurer 2020

import datetime # An included library with Python install.
import re # An included library with Python install.
import csv #An included library with Python install.
import ezgmail #You will have to install this.
# import chromedriver_autoinstaller #You will have to install this

####################### DUES CUTOFFS AND FILES NAMES AND OTHER PREPROCESSING#################################

ten_dues_date = 0
fifteen_dues_date = 0

today = str(datetime.datetime.now()).split('-')
year = int(today[0])
month = int(today[1])
day = int(today[2][:2])
semester = ''
if month <= 12 and month >= 8: #fall semester lies between August and December
	semester = 'fall'
	ten_dues_date = datetime.date(year, 8, 20)
	fifteen_dues_date = datetime.date(year, 1, 1) #start of the previous spring semester
else:
	semester = 'spring'
	ten_dues_date = datetime.date(year, 1, 1)
	fifteen_dues_date = datetime.date(year-1, 8, 10) #start of the previous fall semester



duesFinder = re.compile(r'([A-z]+( [A-z]*)* [A-z]+) paid you (\$10.00|\$15.00)') #A regular expression that matches to suspected dues payments
#group 1 of the regex is the name, group 3 is the value

descrFinder = re.compile(r'paid[<//b>]+ You (.+)Transfer') #matches descriptions of payments inside of the gmailMessage object

# Scraping the email account #
def scrape():
	paymentList = {}
	venmo_data_threads = ezgmail.search('from:venmo (completed OR paid) newer:' + str(fifteen_dues_date), maxResults = 1000)
	#looks through every venmo payment that was either completed or paid that is newer than the dues date
	semesterPayments = 0
	yearPayments = 0
	for i in venmo_data_threads:
		possible_dues_payment = str(i.messages[0].subject) #all the basic subjects containing people's payments
		date = i.messages[0].timestamp.date()
		try:
			descr = str(i.messages[0])
		except:
			descr = str(i.messages[0]).encode('utf-8') #fucking stupid emojis breaking my code GODDAMNIT

		descr = descr.lower() #make it lowercase to get rid of all capitalizations

		# if 'dues' not in descr:
		# 	continue
		# this is a restrictive version of the current code
		
		if 'diplo' in descr or '+1' in descr or 'plus 1' in descr or 'delegation' in descr or 'shirt' in descr or 'tshirt' in descr or 'guest' in descr or 't-shirt' in descr or 'merch' in descr or 'delegate' in descr or 'vamun' in descr or 'register' in descr or 'registration' in descr or 'donation' in descr or 'vics' in descr or 'fundraiser' in descr or 'dome' in descr or '50th' in descr or 'vigmun' in descr or 'fig' in descr or 'dinner' in descr:
		# Do not count diplo ball or VAMUN payments or other stuff as dues payments!
		# PLEASE DO NOT PUT NUMBERS AS PART OF THIS LIST OF STRINGS -- Venmo IDs that are numeric are part of
		# the string that this list of conditions is checked against, and so putting numbers as
		# part of this list will stop some things from being included in the DPM list.
			continue

		for match in duesFinder.finditer(possible_dues_payment):
			amt = int(float(match.group(3).replace('$','')))
			try:
				if (amt == 15 and date > fifteen_dues_date) or (amt == 10 and date > ten_dues_date): #Checks for dues payment
					paymentList[match.group(1)] += amt #throws an error if that dictionary entry doesn't exist
					if date > ten_dues_date:
						semesterPayments += amt #payment was made during this semester
					yearPayments += amt #payment was made sometime in the last year
			
			except: #except statement exists to make sure that I don't have to check when things have to be added to a dictionary
				if (amt == 15 and date > fifteen_dues_date) or (amt == 10 and date > ten_dues_date): #Checks for dues payment
					paymentList[match.group(1)] = amt #adding to a dictionary does so with replacement (so no double counting)
					if date > ten_dues_date:
						semesterPayments += amt
					yearPayments += amt

	return paymentList, semesterPayments, yearPayments

def print_dict(d):
    # loop through the dictionary and print it looking pretty
    for key, value in d.items():
        print(f'{key}: {value}')

def get_dues_past_2_semesters(thing):
    if not isinstance(thing, dict):
        raise TypeError("Function needs a dictionary")
    total_amount = 0
    for pain in thing.keys():
        total_amount += thing[pain]
    return total_amount
        


if __name__ == '__main__':
    print("Scraping the email account:")
    dpm, semesterTotal, yearTotal = scrape()
    #print("Completed scraping the account.")
    print("- There are currently "+str(len(dpm))+" dues paying members.") # num DPMs
    print("- Dues made $"+str(get_dues_past_2_semesters(dpm))+" the last two semesters.") # how much made over a year
    print("- Dues made $"+str(semesterTotal)+" this semester.") # how much made this semester
    print("Here's the full DPM list:")
    print_dict(dpm) # prints full dpm list in a readable way
    

    
