import os
import csv

current_dir = os.getcwd()
excel_file = os.path.join(current_dir, "Resources", "budget_data.csv")

date = []
budget = []
delta_change = []
greatest_date = []

total_money = 0

with open(excel_file) as csvfile:
    excel_reader = csv.reader(csvfile, delimiter=',')

    print(excel_reader)
    csv_header = next(excel_reader)

    prev_month = 0
    month_count = 0

    #Count months and store each date/budget into a list and sum total money
    for row in excel_reader:
        month_count = month_count + 1
        date.append(row[0])
        budget.append(row[1])
        total_money = total_money + int(row[1])

    #Store month to month changes in a list starting after the 1st month
        if month_count>1:
            delta_change.append(int(row[1])-prev_month)
            greatest_date.append(row[0])

        prev_month = int(row[1])

#(1 less delta than the number of total months)
average_delta = sum(delta_change)/(month_count-1)

greatest_increase = 0
greatest_decrease = 0
increase_index = 0
decrease_index = 0

#Calculate the greatest increase and decrease through a for loop
for j in range(len(delta_change)):
    if greatest_increase < delta_change[j]:
        greatest_increase = delta_change[j]
        increase_index = j
    elif greatest_decrease > delta_change[j]:
        greatest_decrease = delta_change[j]
        decrease_index = j

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_money))
print("Average Change: $" + str(round(average_delta,2)))
print("Greatest Increase in Profits: " + str(date[increase_index+1]) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(date[decrease_index+1]) + " ($" + str(greatest_decrease) + ")")

#Print to a txt file
f = open("analysis\output.txt", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.write("Total Months: " + str(month_count))
f.write('\n')
f.write("Total: $" + str(total_money))
f.write('\n')
f.write("Average Change: $" + str(round(average_delta,2)))
f.write('\n')
f.write("Greatest Increase in Profits: " + str(date[increase_index+1]) + " ($" + str(greatest_increase) + ")")
f.write('\n')
f.write("Greatest Decrease in Profits: " + str(date[decrease_index+1]) + " ($" + str(greatest_decrease) + ")")
f.close()