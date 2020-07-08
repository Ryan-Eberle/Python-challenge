# dependencies
import os
import csv

#create path to folder
Election = os.path.join('Resources','election_data.csv')

#open and read the file
with open(Election, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	#need to skip header
	csvhead = next(csvreader)

	#lists and variables for data storage
	candidates = {}
	votes = []
	votes_cand = 0
	total_votes = 0
	percent_votes = 0
	most_votes = 0

	# for loop through data to collect candidates and votes
	for row in csvreader:

		candidate = row[2]
		#add votes to list
		votes.append(total_votes)
		total_votes +=1

		#seperate out candidates
		if candidate in candidates:
			candidates[candidate] +=1
		else:
			candidates[candidate] = 1

#count votes for each candidate
for candidate in candidates:

	if candidates[candidate] > most_votes:
		most_votes = candidates[candidate]
		winner = candidate

print('Election Results')
print('~'*30)
print('Total Vote Count:' +str(total_votes))
print('~'*30)

#calculate percent of votes for each candidate
for candidate in candidates:
	percent_votes = (candidates[candidate])/total_votes *100
	percent_votes = "{}% ".format(round(percent_votes,3))
	print(f'{candidate}: {percent_votes} ({candidates[candidate]}')

print('~'*30)
print('Election Winner:' +str(winner))
print('~'*30)	

#write text file to Analysis folder
#set location
outputplace = os.path.join('Analysis', 'Election_Results.txt')

#open file with write
with open(outputplace, 'w', newline='') as datafile:
	txtwriter = csv.writer(datafile, delimiter= ' ')

	txtwriter.writerow(['Election Results'])
	txtwriter.writerow(['~'*30])
	txtwriter.writerow(['Total Votes:', (total_votes)])
	txtwriter.writerow(['~'*30])

	for candidate in candidates:
		percent_votes = (candidates[candidate])/total_votes*100
		percent_votes = "{}%".format(round(percent_votes,3))
		txtwriter.writerow([f'{candidate}: {percent_votes} ({candidates[candidate]})'])


	txtwriter.writerow(['~'*30])
	txtwriter.writerow(['Election Winner:',winner])
	txtwriter.writerow(['~'*30])
















