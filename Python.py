#The date we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates that recieved votes
#3. The percentage each each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote

import csv
import os
#variable of data being pulled from
file_to_load = os.path.join('election_results.csv')

#variable to save file to path
file_to_save = os.path.join("election_analysis.txt")

#voter counter
total_votes = 0

#candidate names
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results to read file
with open(file_to_load,"r") as election_data:
 file_reader = csv.reader(election_data, delimiter = ",")
 
#print headers
 headers = next(file_reader)

#print each row 
 for row in file_reader:
  #adding to total vote
  total_votes += 1
  
  #print name for each row
  candidate_name = row[2]

  #if candidate does not match
  if candidate_name not in candidate_options:
      candidate_options.append(candidate_name)
      candidate_votes[candidate_name] = 0
  candidate_votes[candidate_name] += 1

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate in candidate_votes:
     votes = candidate_votes[candidate]
     vote_percentage = float(votes) / float(total_votes) *100

    candidate_results = (
        f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)
    txt_file.write(candidate_results)

    if (votes > winning_count) and (vote_percentage > winning_percentage):
       winning_count = votes
       winning_candidate = candidate
       winning_percentage = vote_percentage


winning_candidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n")
   
print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)
