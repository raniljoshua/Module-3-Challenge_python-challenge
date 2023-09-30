#Ranil Joshua, Module 3 Challenge, PyBank

# Modules
import os
import csv

months = 0
net_total = 0
#Dictionary for changes (Diff) in Profit/Losses and corresponding Date
changes = {
    "Date":[],
    "Diff":[]
}
#Greatest increase in profits
greatest_inc_amt = 0
greatest_inc_date = ""
#Greatest decrease in profits
greatest_dec_amt = 0
greatest_dec_date = ""

#Path for budget_data.csv
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV file 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    prev_amount = 0
    for row in csvreader:
        months += 1
        net_total += int(row[1])
        #Appending Date and change (Diff) in Profit/Losses to changes dictionary
        changes["Date"].append(row[0])
        changes["Diff"].append(int(row[1])-prev_amount)
        prev_amount = int(row[1])
    
total_changes = 0
for x in range(1,len(changes["Diff"])):
    # print(changes_two["Diff"][x])

    #total_changes = sum of all changes in profit/losses
    total_changes += changes["Diff"][x]
    #Finding greatest increase in profits (amount and date)
    if changes["Diff"][x] > 0 and changes["Diff"][x] > greatest_inc_amt:
        greatest_inc_amt = changes["Diff"][x]
        greatest_inc_date = changes["Date"][x]
    #Finding greatest decrease in profits (amount and date)
    elif changes["Diff"][x] < 0 and changes["Diff"][x] < greatest_dec_amt:
        greatest_dec_amt = changes["Diff"][x]
        greatest_dec_date = changes["Date"][x]

#Calculating average change in Profit/Losses
average_change = round((total_changes/(len(changes["Diff"])-1)),2)

# print(months)
# print(net_total)
# print(average_change)
# print(greatest_inc_date,greatest_inc_amt)
# print(greatest_dec_date,greatest_dec_amt)

# print('Financial Analysis')
# print('----------------------------')
# print(f'Total Months: {months}')
# print(f'Total: ${net_total}')
# print(f'Average Change: ${average_change}')
# print(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_amt})')
# print(f'Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_amt})')

lines = []
lines.append('Financial Analysis')
lines.append('----------------------------')
lines.append(f'Total Months: ' + str(months))
lines.append(f'Total: $' + str(net_total))
lines.append(f'Average Change: $' + str(average_change))
lines.append(f'Greatest Increase in Profits: ' + greatest_inc_date + ' ($' + str(greatest_inc_amt) + ')')
lines.append(f'Greatest Increase in Profits: ' + greatest_dec_date + ' ($' + str(greatest_dec_amt) + ')')

for line in lines:
    print(line)

#Python write to file: https://www.pythontutorial.net/python-basics/python-write-text-file/
with open('Analysis/Financial Analysis.txt','w') as f:
    f.writelines('\n'.join(lines))
