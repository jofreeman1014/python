# -*- coding: utf-8 -*-
"""
* In this challenge, you are tasked with helping a small, rural town modernize 
its vote-counting process. (Up until now, Uncle Cleetus had been trustfully 
tallying them one-by-one, but unfortunately, his concentration isn't what it 
used to be.)
* You will be give a set of poll data called 
[election_data.csv](PyPoll/Resources/election_data.csv). 
The dataset is composed of three columns: `Voter ID`, `County`, and 
`Candidate`. Your task is to create a Python script that analyzes the votes 
and calculates each of the following:

  
* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal 
and export a text file with the results.
"""

#Initialize and Import
import csv
import os

ed_file = os.path.join("Resources","election_data.csv")

'''
Record and collect:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
'''

#Define vars to contain results
vote_tot = 0
candidate = []
vote_per = [] # vote percentage 
tot_cand = [] #candidate individual totals
winner = 0

#%%
#Populate Candidate List
with open(ed_file, "r", newline="") as ed_data:
    reader = csv.reader(ed_data)
    header = next(reader)
    for row in reader: # Initializing candidate list
        vote_tot += 1 # ezbake row counter for later
        if row[2] not in candidate:
            candidate.append(row[2])
            
#%%
# Initializing vote_per_candidate
for x in range(len(candidate)):
    tot_cand.append(0)
    
with open(ed_file, "r", newline="") as ed_data: # re-initialize reader
    reader = csv.reader(ed_data)
    header = next(reader)
    for row in reader: # count votes individually w/ name matching
        for i in range(len(candidate)): 
            if row[2] == candidate[i]:
                tot_cand[i] += 1
for i in range(len(tot_cand)):
    vote_per.append(round((100*(tot_cand[i])/vote_tot),4))
    
winner = candidate[tot_cand.index(max(tot_cand))]
    
#%%
# Reporting and Exporting
'''
* In addition, your final script should both print the analysis to the terminal 
and export a text file with the results.
'''
output = open("PyPoll.txt","w")
text = (f"Election Results\n====================\nTotal Votes: {vote_tot}\n====================")
for x in range(len(candidate)):
    text += (f"\n{candidate[x]}: {vote_per[x]}% ({tot_cand[x]})")
text += (f"\n====================\nWinner: {winner}\n====================")
output.write(text)
print(text)
