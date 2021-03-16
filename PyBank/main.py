# Import the os Module to creat file path
import os
# Moudle for reading CSV file
import csv
# Specify the file to write to
csvpath = os.path.join('Resources', 'budget_data.csv')
# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")  
# Read each row of data after the header
    for row in csvreader:
        print(row)
# Total number of months included in the dataset
        row_count = []
        row_count.append(row)
        print(row_count)
# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

#The greates increase in profits (date and amount) over the entire period

#the greatest decrease in losses (date and amount) over the entire period
