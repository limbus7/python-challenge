# First we’ll import us module
# This will allow us to create file path across operating systems
import os
# Module for reading CSV files
import csv

votePerCandidate = []
profitOrLoss = []

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#read from csv
with open(csvpath) as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if(row[2] != 'Candidate'):
            votePerCandidate.append(row[2])


#each record is candidate's name which represent a vote
totalVotes = len(votePerCandidate) 

candidates = {} # container to store votes for each candidate

#loop through all votes
for i in range(0, totalVotes):
    # increase the vote count for the candidate if they are present in the dict else create record with 1 vote
    if votePerCandidate[i] in candidates:
        candidates[votePerCandidate[i]] = candidates[votePerCandidate[i]] +1
    else:
        candidates[votePerCandidate[i]] = 1

#variables to keep track of winner
winner = ""
winnersVote = 0

#Accumulate output
output = "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {totalVotes}\n"
output += "-------------------------\n"

#loop through each candidate to display their votes and find the winner
for candidate, vote in candidates.items():
    if vote > winnersVote: # find winner
        winnersVote = vote
        winner = candidate
    votePercent = round((vote*100)/totalVotes,3)
    output += f"{candidate}: {votePercent}% ({vote})\n"
output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += f"-------------------------\n"

print(output) # display in console
#write output in file
f = open("../analysis/PyPollResult.txt", "w")
f.write(output)
f.close()