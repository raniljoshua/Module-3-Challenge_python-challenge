#Ranil Joshua, Module 3 Challenge, PyPoll

# Modules
import os
import csv

total_votes = 0
candidate = {
    "Name":[],
    "Votes":[],
    "Percent Votes":[]
}

prev_candidate = ""
num_votes = 0

#Path for budget_data.csv
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV file 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        #If we encounter the new candidate name
        if row[2] in candidate["Name"]:
            candidate["Votes"][candidate["Name"].index(row[2])] += 1
        else:
            candidate["Name"].append(row[2])
            candidate["Votes"].append(int(1))


for x in candidate["Votes"]:
    candidate["Percent Votes"].append(round((x/total_votes*100),3))

winner = candidate["Name"][candidate["Votes"].index(max(candidate["Votes"]))]

# print(total_votes)
# print(candidate)
# print(winner)

# print('Election Results')
# print('------------------------')
# print('Total Votes: ' + str(total_votes))
# print('------------------------')
# for x in range(0,len(candidate["Name"])):
#     print(candidate["Name"][x] + ': ' + str(candidate["Percent Votes"][x]) + "% (" + str(candidate["Votes"][x]) + ")")
# print('------------------------')
# print('Winner: ' + winner)

lines = []
lines.append('Election Results')
lines.append('------------------------')
lines.append('Total Votes: ' + str(total_votes))
lines.append('------------------------')
for x in range(0,len(candidate["Name"])):
    lines.append(candidate["Name"][x] + ': ' + str(candidate["Percent Votes"][x]) + "% (" + str(candidate["Votes"][x]) + ")")
lines.append('------------------------')
lines.append('Winner: ' + winner)
lines.append('------------------------')


for line in lines:
    print(line)

# #Python write to file: https://www.pythontutorial.net/python-basics/python-write-text-file/
with open('Analysis/Election Results.txt','w') as f:
    f.writelines('\n'.join(lines))