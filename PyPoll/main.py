#Import Modules
import os
import csv

#Start Variables
vote_count=0
candidates=[]
votes=[]

#Import Election Data
csv_name = "election_data.csv"
with open(csv_name) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header=next(election_data)

#Loop through all rows
    for row in election_data:
        
        #Add New Candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
        #Add Votes
        votes[candidates.index(row[2])]=votes[candidates.index(row[2])]+1

#Calculate Percentages
percentage=[x / sum(votes) for x in votes]
#Calculate Winner
winnerno=votes.index(max(votes))
winner=candidates[winnerno]

#Write Results
f= open("election_analysis.txt","w+")
print("Total Votes",sum(votes),file=f)

for i in range (0,len(candidates)):
    print(candidates[i],int(round(percentage[i]*100,0)),"%",votes[i],file=f)

print("Winner:",winner,file=f)

#Print Results
print("Total Votes",sum(votes))

for i in range (0,len(candidates)):
    print(candidates[i],int(round(percentage[i]*100,0)),"%",votes[i])

print("Winner:",winner)

