# import dependencies
import os
import csv

# create a function that will print to both terminal and to the result.txt file at the same time
def output_loops():
    prints=["Election Results",
        "----------------------------------",
        f'Total Votes: {total_votes}',
        "----------------------------------",
        f'Charles Casper Stockham: {ccs_ratio}% ({ccs_count})',
        f'Diana DeGette: {dd_ratio}% ({dd_count})',
        f'Raymon Anthony Doane: {rad_ratio}% ({rad_count})',
        "----------------------------------",
        f"Winner: {max_ratio}",
        "----------------------------------"
    ]

    output_folder = 'analysis'
    output_file = 'result.txt'
    output_path = os.path.join(output_folder, output_file)
    
    with open(output_path, 'w') as file:
        for i in prints:
            file.write(i + '\n')
            print(i)

voter_id = []
county = []
candidate = [] 

# create a file path to allow us to read and store the contents of the CSV file within the lists
poll_data_csv = os.path.join("Resources","election_data.csv")

with open(poll_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# create an empty list and a for loop that will identify the unique candidates
unique_candidates = []

for item in candidate:
       if item not in unique_candidates:
            unique_candidates.append(item)
#count total votes
total_votes = len(voter_id)

#count section 
ccs_count = candidate.count("Charles Casper Stockham")
dd_count = candidate.count("Diana DeGette")
rad_count = candidate.count("Raymon Anthony Doane")

#ratio section: calculate the percentages 
ccs_ratio = round((ccs_count/total_votes)*100, 3)
dd_ratio = round((dd_count/total_votes)*100, 3)
rad_ratio = round((rad_count/total_votes)*100, 3)

# winner count 
total_ratios = {"Charles Casper Stockham":ccs_ratio, "Diana DeGette":dd_ratio, "Raymon Anthony Doane":rad_ratio} 

max_ratio = max(total_ratios, key=lambda x: total_ratios[x])

output_loops()
            