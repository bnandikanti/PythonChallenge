import os
import csv
date = []
totalValues = []
changes = []
budget_csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    # Read through each row of data after the header and increase the count to get the total number of rows
    # Get the count for total months, date and total the amount of all the values and place these in 3 lists
    count = 0
    total = 0
    for row in csv_reader:
        count = count + 1
        date.append(row[0])
        totalValues.append(row[1])
    for itemValue in totalValues:
        total = total + int(itemValue)
    
    
#Calculate change and add it to a list
averagechange = 0
for index in range(len(totalValues)- 1):
    change = int(totalValues[index + 1]) - int(totalValues[index])
    changes.append(change)


# Get the greatest and least values for the change
greatestIncrease = max(changes)
greatestDecrease = min(changes)
#Get the index for these values 
greatestIncreaseIndex = changes.index(greatestIncrease)
greatestDecreaseIndex = changes.index(greatestDecrease)

#Use the index number from above to get the values from the date list
print("Financial Analysis \n")
print("--------------------------------- \n")
print("Total Months : " + str(count))
print("Total: $"+str(total))
print("Average Change: $" + str(round(sum(changes)/85, 2)))
print(f"Greatest Increase in Profits: {date[greatestIncreaseIndex + 1]}  (${max(changes)})")
print(f"Greatest Decrease in Profits: {date[greatestDecreaseIndex + 1]}  (${min(changes)})")

#Writing output to text file
textfile = open('output/PyBank.txt', "w")
textfile.write("Financial Analysis \n")
textfile.write("---------------------------------\n")
textfile.write("Total Months: " + str(count)+ "\n")
textfile.write("Total: $" +str(total)+"\n")
textfile.write("Average Change : $" +str(round(sum(changes)/85, 2))+"\n")
textfile.write("Greatest Increase in Profits: " + str(date[greatestIncreaseIndex + 1])  + " ($" +str(max(changes)) + ")\n")
textfile.write("Greatest Increase in Profits: " + str(date[greatestDecreaseIndex + 1])  + " ($" +str(min(changes)) + ")\n")
     
    