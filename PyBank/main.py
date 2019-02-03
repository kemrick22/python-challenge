#Import Modules
import os
import csv

#Start Stat Tracking Variables
month_count=0
total_profit_loss=0
max_profit=0
min_profit=0
total_change=0
change=0
last_month=0

#Import Budget Data
csv_name = "budget_data.csv"
with open(csv_name) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    header=next(budget_data)

#Loop through all rows
    for row in budget_data:
        
        #Count Month
        month_count += 1
        #Count Total Profit
        total_profit_loss += int(row[1])
        #Track Change
        if month_count==1:
            pass
        else:
            change=(int(row[1])-last_month)
            total_change+=change
        #Track Max
        if change>max_profit:
            max_profit=change
            max_date=row[0]
        #Track Min
        if change<min_profit:
            min_profit=change
            min_date=row[0]
        #Save P/L as Last Month
        last_month=int(row[1])

#Calculate Average Change
average_change=round(total_change/(month_count-1),2)

#Write Results
f= open("budget_analysis.txt","w+")
print("Total Months: ", str(month_count),file=f)
print("Total P/L: $", str(total_profit_loss),file=f)
print("Average Change: $", str(average_change),file=f)
print("Greatest Increase: ", max_date,"$", str(max_profit),file=f)
print("Greatest Decrease: ", min_date,"$", str(min_profit),file=f)

#Print Results
print("Total Months: ", str(month_count))
print("Total P/L: $", str(total_profit_loss))
print("Average Change: $", str(average_change))
print("Greatest Increase: ", max_date,"$", str(max_profit))
print("Greatest Decrease: ", min_date,"$", str(min_profit))
