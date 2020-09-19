import os
import csv

input_file = os.path.join("Resources","election_data.csv")
output_file = os.path.join("analysis","poll_analysis.txt")

voter_id = []
candidate_list = []
poll = {}
with open(input_file) as poll_data:
    reader = csv.reader(poll_data, delimiter = ',')
    header = next(reader)

    for row in reader:
        voter_id.append(row[0])
        candidate_list.append(row[2])


for candidate in candidate_list:
    if (candidate in poll):
        poll[candidate] += 1
    else:
        poll[candidate] = 1

total_votes = len(voter_id)   
winner = max(poll, key=poll.get)

output = (
    f"\nElection Results\n"
    f"----------------------------\n"
      
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n" )
for key, value in poll.items():
    percent_vote = "{:.3f}".format(value / total_votes * 100)         
    output += (f"{key} : {percent_vote}% ({value})\n" )
output += (f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n" )   
print(output)
with open(output_file, "w") as txt_file:
    txt_file.write(output)   
