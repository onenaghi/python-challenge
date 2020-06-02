#Import Modules
import os
import csv

#Read CSV File
csvpath = os.path.join('Resources','budget_data.csv')

# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')

#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")
    
#     for row in csvreader:
#         print(row)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # The total number of months included in the dataset

    months = []
    csv_header = next(csvreader)
    for row in csvreader:
        # print(row)
        months.append(row[0])
    # print(months)
    num_of_mon = (len(months))
    print(f'Total number of Months: {num_of_mon}')
    
    # The net total amount of "Profit/Losses" over the entire period

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    net_profit = 0
    csv_header = next(csvreader)
    #print(csv_header[1])
    for row in csvreader:
        #print(row[1])
        net_profit = net_profit + int(row[1])
    # print(f'Net profit: {net_profit}')
   
    

# The average of the changes in "Profit/Losses" over the entire period

avg_change = net_profit/num_of_mon
#print(f'Average change per month: {avg_change}')

#Nicer Format
net_profit = '${:,.2f}'.format(net_profit)
print(f'Net profit: {net_profit}')
avg_change = '${:,.2f}'.format(avg_change)
print(f'Average change per month: {avg_change}')

# The greatest increase in profits (date and amount) over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #print(csv_header[1])
    profitpm = []
    for row in csvreader:
        # print(row[1])
        profitpm.append(row[1])
    # print(profitpm)
    # print(max(profitpm))
    # print(profitpm.index(max(profitpm,)))
    max_index = int(profitpm.index(max(profitpm)))
#     print(min(profitpm))
#     print(profitpm.index(min(profitpm)))
    min_index = int(profitpm.index(min(profitpm)))

max_val = int(max(profitpm))
max_val = '${:,.2f}'.format(max_val)
max_date = months[max_index]
min_val = int(min(profitpm))
min_val = '${:,.2f}'.format(min_val)
min_date = months[min_index]
# print(min_val)
# print(max_val)
# print(max_date)
# print(min_date)

print(f'Greatest Increase in profits: {max_val} on {max_date}')
print(f'Greatest Decrease in profits: {min_val} on {min_date}')

#Make lists to store data
list1 = ["Number of Months", "Net Profit", "Average Change in Profit", "Biggest Increase Value","Biggest Increase Date", "Biggest Loss Value", "Biggest Loss Date"]
# print(list1)
list2 = [num_of_mon, net_profit, avg_change, max_val, max_date, min_val, min_date]
# print(list2)
zipped_data = zip(list1, list2)

output_path = os.path.join("Analysis", "output_file.csv")
with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(zipped_data)