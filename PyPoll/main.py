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



        
    print("Total Votes:" +str(totalVotes))
    print(Candidates)
    print(Candidates[0] + ": " +str(round((count1/totalVotes)*100, 3)) + "% (" + str(count1) + ")")
    print(Candidates[1] + ": " +str(round((count2/totalVotes)*100, 3)) + "% (" + str(count2) + ")")
    print(Candidates[2] + ": " +str(round((count3/totalVotes)*100, 3)) + "% (" + str(count3) + ")")
    print(Candidates[3] + ": " +str(round((count4/totalVotes)*100, 3)) + "% (" + str(count4) + ")")
    
    VotesForPerson = [count1, count2, count3, count4]
    print("Winner: " + str(max(count1, count2, count3, count4)))
    #print(
    #print("Percentage: " +str((totalVotes/Candidates.count) * 100))
