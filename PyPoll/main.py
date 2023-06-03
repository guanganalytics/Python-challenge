import os
import csv


print("Election Results")
print("")
print("--------------------------------------------")


csvpath=r"C:\Users\henry\Desktop\Python-challenge\PyPoll\Resources\election_data.csv"

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    total_votes=0
    candidate_list=[]
    for row in csvreader:
# The total number of votes cast
        total_votes=total_votes+1
# A complete list of candidates who received votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
print("")
print("Total Votes: "+str(total_votes))
print("")
print("--------------------------------------------")

# The percentage of votes and the total votes each candidate won
#since we need the full candidate list and total votes in the next calculation, I did not have the next step including into the first loop
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

   
    candidate_0_length=[]
    candidate_1_length=[]
    candidate_2_length=[]
    candidate_0_total=0
    candidate_1_total=0
    candidate_2_total=0

    for row in csvreader:
        if row[2]==candidate_list[0]:
            candidate_0_total=candidate_0_total+1
        elif row[2]==candidate_list[1]:
            candidate_1_total=candidate_1_total+1
        elif row[2]==candidate_list[2]:
            candidate_2_total=candidate_2_total+1

    candidate_0_percentage=candidate_0_total/total_votes*100
    candidate_1_percentage=candidate_1_total/total_votes*100
    candidate_2_percentage=candidate_2_total/total_votes*100
    formattedcandidate_0_percentage = f"{candidate_0_percentage:.3f}%"
    formattedcandidate_1_percentage = f"{candidate_1_percentage:.3f}%"
    formattedcandidate_2_percentage = f"{candidate_2_percentage:.3f}%"


print("")
print(candidate_list[0]+": "+str(formattedcandidate_0_percentage)+" ("+str(candidate_0_total)+")")
print("")
print(candidate_list[1]+": "+str(formattedcandidate_1_percentage)+" ("+str(candidate_1_total)+")")
print("")
print(candidate_list[2]+": "+str(formattedcandidate_2_percentage)+" ("+str(candidate_2_total)+")")
print("")
print("--------------------------------------------")

# The winner of the election based on popular vote
if candidate_0_total>candidate_1_total and candidate_0_total>candidate_2_total:
    winner=candidate_list[0]
elif candidate_1_total>candidate_0_total and candidate_1_total>candidate_2_total:
    winner=candidate_list[1]
elif candidate_2_total>candidate_0_total and candidate_2_total>candidate_1_total:
    winner=candidate_list[2]
print("")
print("Winner: "+str(winner))
print("")
print("--------------------------------------------")

my_string=f"""Election Results

--------------------------------------------

Total Votes: {total_votes}

--------------------------------------------

{candidate_list[0]}: {formattedcandidate_0_percentage} ({candidate_0_total})

{candidate_list[1]}: {formattedcandidate_1_percentage} ({candidate_1_total})

{candidate_list[2]}: {formattedcandidate_2_percentage} ({candidate_2_total})

--------------------------------------------

Winner: {winner}

--------------------------------------------"""

with open("PyPoll.txt","w") as f:
    f.write(my_string)

       