
import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

dates = []
profit_change = []
total = 0

with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
#     reading header
    header = next(reader)
    
#     reading first row of data
    first_row = next(reader)
    dates.append(first_row[0])  # adding first row date to dates list
    prev = int(first_row[1])  # initializing previous profit to first row
    total += int(first_row[1])  # initializing total profit to first row


#     loop through each row from second row of data
    for row in reader:
        dates.append(row[0])  # adding each row to dates list
        
        profit_change.append(int(row[1]) - prev)  # adding profit change values to a list
        prev = int(row[1])  # making current row value as previous profit 

        total += int(row[1])  # adding each month's profit to total profit
        
# calculations   

total_months = len(dates)

# average change
avg_change = round(sum(profit_change) / len(profit_change), 2)  

# greatest increase
max_change = max(profit_change)
max_change_month = dates[profit_change.index(max_change) + 1]  # (index + 1) is done considering the first row, where profit change is not calculated

# greatest decrease
min_change = min(profit_change)
min_change_month = dates[profit_change.index(min_change) + 1]  # (index + 1) is done considering the first row

# formatting the output to display
output = (    
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {max_change_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_change_month} (${min_change})\n")

# print the output to terminal
print(output)

# write output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)   
    
