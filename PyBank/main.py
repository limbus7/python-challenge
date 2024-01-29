# First we’ll import us module
# This will allow us to create file path across operating systems
import os
# Module for reading CSV files
import csv

months = []
profitOrLoss = []

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#read from csv
with open(csvpath) as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if(row[1] != 'Profit/Losses'):
            months.append(row[0])
            profitOrLoss.append(int(row[1]))

totalRecord = len(months) # total record
print(profitOrLoss[2])
# Initilize variables
sum=0
totalChange = 0

#set first values as default
greatestIncrease = profitOrLoss[1] - profitOrLoss[0] 
greatestIncreaseMonth = months[1]
greatestdecrease = profitOrLoss[1] - profitOrLoss[0]
greatestDecreaseMonth = months[1]

#loop through record to get desired output
for key in range(len(profitOrLoss)):
    if(key!=0): #skip first record to calculate change
        change = profitOrLoss[key] - profitOrLoss[key-1]
        if(change>greatestIncrease):
            greatestIncrease = change
            greatestIncreaseMonth = months[key]
        if(change<greatestdecrease):
            greatestdecrease = change
            greatestDecreaseMonth = months[key]
        totalChange += change
    sum+=profitOrLoss[key]
averageChange = round(totalChange/(totalRecord-1),2)

# accumulate output to display later
output = "Financial Analysis\n"
output += "----------------------------\n"
output += f"Total Months: {totalRecord}\n"
output += f"Total: ${sum}\n"
output += f"Average Change: ${averageChange}\n"
output += f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n"
output += f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestdecrease})\n"

print(output) # display in console
#write output in file
f = open("../analysis/PyBankOutput.txt", "w")
f.write(output)
f.close()