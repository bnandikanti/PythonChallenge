import os
import csv

cereal_csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    # Read through each row of data after the header and increase the count to get the total number of rows
    count = 0
    for row in csv_reader:
        count = count + 1
    print("Total Months : " + str(count))
