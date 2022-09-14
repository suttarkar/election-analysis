# Add Dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources module 3", "election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    

# Close the file.
election_data.close()