import os
import csv

input_file = os.path.join("Resources","election_data.csv")
output_file = os.path.join("analysis","poll_analysis.txt")

# initializing empty lists
voter_id = []
candidate_list = []

# initializing empty dictionary
poll = {} 

# reading the input file and storing needed columns as lists
with open(input_file) as poll_data:
    reader = csv.reader(poll_data, delimiter = ',')
    header = next(reader)

    for row in reader:
        voter_id.append(row[0])
        candidate_list.append(row[2])

# calculating frequency of occurance of each candidate in candidate_list to poll dictionary
for candidate in candidate_list:
    if (candidate in poll):
        poll[candidate] += 1
    else:
        poll[candidate] = 1

# calculating total votes
total_votes = len(voter_id)   

#finding winner by getting the key paired with the max value in poll directory
winner = max(poll, key=poll.get)

# formatting the output string
output = (
    f"\nElection Results\n"
    f"----------------------------\n"
      
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n" )

# loop through the keys and values in the dictionary and appending them to the output string
for key, value in poll.items():
    percent_vote = "{:.3f}".format(value / total_votes * 100)         
    output += (f"{key} : {percent_vote}% ({value})\n" )

# outside the loop appending final result to the output string
output += (f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n" )   

#print output on terminal
print(output)

#write output to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output) 
