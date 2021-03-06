# Get dependencies
import os
import csv
from collections import Counter

# Path to collect data from the Resources folder
csv_path = os.path.join('..', 'PyPoll/Resources', 'election_data.csv')

# Read the csv with DictReader to get Header Row as dictionary key-value references

with open(csv_path) as csvfile:
    vote_reader = csv.DictReader(csvfile, delimiter=',')
    count_Candidate = {}

# Count the the number of times each Candidate is duplicated in "Candidate" column


    for row in vote_reader:
        entry = dict(row)
        if entry['Candidate'] in count_Candidate:
            count_Candidate[entry['Candidate']] +=1
        else:
            count_Candidate[entry['Candidate']] = 1

# while with the new dictionary, sort it using Lambda function and then apply reverse sort to show winner first


    sorted_Candidate = dict(sorted(count_Candidate.items(), key=lambda val:val[1], reverse=True))

# get list of dictionaries and find total votes


    vote_rows = []
    with open(csv_path) as csvfile:
        vote_reader = csv.DictReader(csvfile, delimiter=',')
        for row in vote_reader:
            vote_rows.append(row)
    total_votes = len(vote_rows)

 # use dictionary comprehension to specify winner from sorted dictionary


winner = [key for key in sorted_Candidate.keys()][0]

# f-strings for output to terminal
message1 = (f"Election Results\n"
f"-----------------------------------\n"
f"Total Votes: {total_votes}\n"
f"-----------------------------------\n")
print(message1)

# use loop through dictionary to find percentages and round them to two decimal places


for k, v in sorted_Candidate.items():
    percent = []
    percent = round(((int(v)/total_votes)*100), 2)
    results_summary = (f'{k}: {percent}% with ({v}) votes')
    print(results_summary)


message2 = (f"\n"
f"-----------------------------------\n"
f"Winner: {winner}\n"
f"-----------------------------------\n")
print(message2)

# Path to write text file into the "analysis" folder
output_path = os.path.join('..', 'PyPoll/analysis', 'election_results.txt')

# Write to the txt file:
with open(output_path, 'w+') as txtfile:
    # Use print to output file so loop can be repeated for output into text file
    print(message1, file=txtfile)
    for k, v in sorted_Candidate.items():
        percent = []
        percent = round(((int(v)/total_votes)*100), 2)
        results_summary = (f'{k}: {percent}% with ({v}) votes')
        print(results_summary, file=txtfile)
    print(message2, file=txtfile)
    txtfile.close()