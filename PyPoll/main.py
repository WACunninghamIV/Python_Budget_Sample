 Import the os Module to creat file path
import os
# Moudle for reading CSV file
import csv
# Specify the file to write to
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")  
# Read each row of data after the header
for row in csvreader:
        print(row)
#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.
