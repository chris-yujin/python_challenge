#import dependencies
import csv
import os

#create a function to print to terminal and to result.txt file 
def output_loops():

    prints=["Financial Analysis", 
        "----------------------------------------------------------", 
        f"Total Months: {str(month_cnt)}", 
        f"Total: {str(net_pl)}",
        f"Average Change: ${str(avg_change)}",
        f"Greatest Increase in Profits: {date_most} (${most})",
        f"Greatest Decrease in Profits: {date_least} (${least})"
    ]

    output_folder = 'analysis'
    output_file = 'result.txt'
    output_path = os.path.join(output_folder, output_file)
    
    with open(output_path, 'w') as file:
        for i in prints:
            file.write(i + '\n')
            print(i)

date = []
p_l = []
net_pl = 0

#create path to open csv file
budget_data_csv = os.path.join("Resources","budget_data.csv") 

#open and read csv file 
with open(budget_data_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    rows = list(csv_reader)  

# create the date and p_l lists and month count variable
date = [row[0] for row in rows]
p_l = [float(row[1]) for row in rows]
month_cnt = len(date)

#finding out the net profit and loss 
for i in p_l:
    net_pl += i

#Average changes of profit and loss

delta_profit=[]

for i in range(len(p_l) - 1):
    change = p_l[i+1] - p_l[i]
    delta_profit.append(change)
    
avg_change = round(sum(delta_profit)/len(delta_profit),2)

#Greatest increase in profits (date and amount) 
most = 0
least = 0

#Collect the month of the greatest or least profit
date_most = 0 
date_least = 0

for item in delta_profit:
    if item > most:
        most = item
        date_most = date[delta_profit.index(item) + 1]
for item in delta_profit:
    if item < least:
        least = item
        date_least = date[delta_profit.index(item)+ 1]

most = format(most,".0f")
least = format(least,".0f")
net_pl = format(net_pl,".0f")

output_loops()