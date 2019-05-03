import os
import csv
date = []
totalValues = []
Changes = []
budget_csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    # Read through each row of data after the header and increase the count to get the total number of rows
    print("Financial Analysis \n")
    print("--------------------------------- \n")
    count = 0
    total = 0
    for row in csv_reader:
        count = count + 1
        date.append(row[0])
        totalValues.append(row[1])
    print("Total Months : " + str(count))
    for itemValue in totalValues:
        total = total + int(itemValue)
    print("Total: $"+str(total))
    
    averagechange = 0
    for index in range(len(totalValues)- 1):
        Change = int(totalValues[index + 1]) - int(totalValues[index])
        Changes.append(Change)
    print("Average Change: " + str(round(sum(Changes)/85, 2)))

    zippedtuple = []
    zippedtuple = zip(Changes, date)

    for change, date in range(len(zippedtuple)):
        if change == max(Changes):
            print(max(Changes), date[date + 1])

    print("Greatest Increase in Profits: ")


    
    # Read through each row for column 2 except the header, and get the total amount of profit/losses
    
   # total = 0
    #for row in csv_reader:
        #totalValues.append(row[1])
    
    #print("Total: " + str(sum(totalValues)))

    #print(totalValues)