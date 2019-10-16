import os
import csv

# declare variable

total_month = 0
total_sum = 0.00
profit_lost_change = []
ave_profit_lost = 0.00
greatest_Increase = 0.00
greatest_Lost = 0.00
last_month_amount = 0.00

csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    
# calculation 1
    for row in csvreader:
        total_month  +=1
        total_sum = total_sum + float(row[1])
        
        if(total_month > 1):
            profit_lost_change.append(float(row[1]) - last_month_amount)  
        
        last_month_amount = float(row[1])
#calulation 2
ave_profit_lost = round(sum(profit_lost_change) / len(profit_lost_change), 2)
greatest_Increase = max(profit_lost_change)
greatest_Lost = min(profit_lost_change)

# print in screen
        
print("Financial Analysis")
print("----------------------------")

print(f"Total Months: {total_month}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${ave_profit_lost}")
print(f"Greatest Increase in Profits: Feb-2012 (${greatest_Increase})")
print(f"Greatest Decrease in Profits: Sep-2013 (${greatest_Lost})")

# writing to text file 

output_file = os.path.join('Financial Analysis.txt')

# 
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n" + "---------------------------\n")
    txtfile.write(f"Total Months: {total_month}\n")
    txtfile.write(f"Total: ${total_sum}\n")
    txtfile.write(f"Average Change: ${ave_profit_lost}\n")
    txtfile.write(f"Greatest Increase in Profits: Feb-2012 (${greatest_Increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: Sep-2013 (${greatest_Lost})\n")

    
