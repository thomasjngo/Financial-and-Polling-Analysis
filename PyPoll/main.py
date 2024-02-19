import os
import csv

current_dir = os.getcwd()
excel_file = os.path.join(current_dir, "Resources", "election_data.csv")

candidate_counter={}

with open(excel_file) as csvfile:
    excel_reader = csv.reader(csvfile, delimiter=',')

    print(excel_reader)
    csv_header = next(excel_reader)

    total_votes = 0

    #Candidate/vote dictionary generator
    for row in excel_reader:

        name = row[2]
        if name in candidate_counter:
            candidate_counter[name]=candidate_counter[name]+1
        else:
            candidate_counter[name]=1

        total_votes = total_votes + 1


print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")

#Loop to print the candidate results with percentage of vote
for key, value in candidate_counter.items():
    print(key + ": " + str(round(((int(value)/total_votes)*100),3)) + "% " + "(" + str(value) + ")")

print("----------------------------")

#Ask dictionary to lookup the max value and return winner
print("Winner: " + str(max(candidate_counter, key=candidate_counter.get)))
print("----------------------------")


#Write results into a txt file
f = open("analysis\output.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.write("Total Votes: " + str(total_votes))
f.write('\n')
f.write("----------------------------")
f.write('\n')

for key, value in candidate_counter.items():
    f.write(key + ": " + str(round(((int(value)/total_votes)*100),3)) + "% " + "(" + str(value) + ")")
    f.write('\n')

f.write("----------------------------")
f.write('\n')
f.write("Winner: " + str(max(candidate_counter, key=candidate_counter.get)))
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.close()