# -*- coding: utf-8 -*-
#Initialize and Import
import csv
import os

ed_file = os.path.join("Resources","election_data.csv")

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
output = open("PyPoll.txt","w")
text = (f"Election Results\n====================\nTotal Votes: {vote_tot}\n====================")
for x in range(len(candidate)):
    text += (f"\n{candidate[x]}: {vote_per[x]}% ({tot_cand[x]})")
text += (f"\n====================\nWinner: {winner}\n====================")
output.write(text)
print(text)
