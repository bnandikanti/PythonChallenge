import os
import csv

Candidates = []
budget_csv_path = os.path.join("..", "Resources", "election_data.csv")

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    # Read through each row of data after the header and increase the count to get the total number of rows
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    totalVotes = 0
    for row in csv_reader:
        totalVotes = totalVotes + 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
        
        if row[2] == Candidates[0]:
            count1 = count1 + 1
        elif row[2] == Candidates[1]:
            count2 = count2 + 1
        elif row[2] == Candidates[2]:
            count3 = count3 + 1
        elif row[2] == Candidates[3]:
            count4 = count4 + 1
    VotesForPerson = {"Khan":count1, "Corey":count2, "Li":count3, "O'Tooley":count4}
    print("Election Results \n")
    print("----------------------------\n")
    print("Total Votes: " +str(totalVotes) +"\n")
    print("----------------------------\n")
    print(Candidates[0] + ": " +str(round((count1/totalVotes)*100, 3)) + "% (" + str(count1) + ")")
    print(Candidates[1] + ": " +str(round((count2/totalVotes)*100, 3)) + "% (" + str(count2) + ")")
    print(Candidates[2] + ": " +str(round((count3/totalVotes)*100, 3)) + "% (" + str(count3) + ")")
    print(Candidates[3] + ": " +str(round((count4/totalVotes)*100, 3)) + "% (" + str(count4) + ")")
    print("----------------------------\n")
    print("Winner : "+ max(VotesForPerson, key=VotesForPerson.get) +"\n")
    print("----------------------------\n")
    
#Writing output to text file
textfile = open('output/PyPoll.txt', "w")
textfile.write("Election Results \n")
textfile.write("---------------------------------\n")
textfile.write("Total Votes: " +str(totalVotes) +"\n")
textfile.write("---------------------------------\n")
textfile.write(Candidates[0] + ": " +str(round((count1/totalVotes)*100, 3)) + "% (" + str(count1) + ")\n")
textfile.write(Candidates[1] + ": " +str(round((count2/totalVotes)*100, 3)) + "% (" + str(count1) + ")\n")
textfile.write(Candidates[2] + ": " +str(round((count3/totalVotes)*100, 3)) + "% (" + str(count1) + ")\n")
textfile.write(Candidates[3] + ": " +str(round((count4/totalVotes)*100, 3)) + "% (" + str(count1) + ")\n")
textfile.write("---------------------------------\n")
textfile.write("Winner : "+ max(VotesForPerson, key=VotesForPerson.get) +"\n")
textfile.write("---------------------------------\n")
