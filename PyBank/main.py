# Start by getting dependencies
import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join('..', 'PyBank/Resources', 'budget_data.csv')


# code block starting with dictionaries after reading CSV file
# Read the csv and skip the Header row
with open(csv_path) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    header = next(budget_reader)
    budget = dict(budget_reader)
    # convert budget values to a list
    profit_loss = list(budget.values())
    months = list(budget.keys())

# Define function for subtotals
profits = list([int(x) for x in profit_loss])       
def subtot(profits):
    subtotals = []
    for i in range(0,len(profits)-1):
        p = profits[i]
        q = profits[i+1]
        r = q - p
        yield(r)
        subtotals.append(r)


# Define function to get Average of monthly profits/losses
subtotals = list(subtot(profits))
def average(subtotals):
    l = len(subtotals)
    total_profits = 0
    for val in subtotals:
        total_profits = total_profits + val
    return(total_profits / l)
# print(f"The average monthly profit was actually a loss of ${round(average(subtotals),2)}.")   

# Path to write text file into the "analysis" folder
output_path = os.path.join('..', 'PyBank/analysis', 'analysis-results.txt')

message = (f"Financial Analysis\n"
f"-----------------------------------\n"
f"Total Profits were ${sum(profits)}.\n"
f"Average Profit Change was ${round(average(subtotals),2)}.\n"
f"Greatest Increase in Profits was ${max(subtot(profits))} which occurred between {months[78]} and {months[79]}.\n"
f"Greatest Decrease in Profits was ${min(subtot(profits))} which occurred between {months[48]} and {months[49]}.")

print(message)

# Write the txt file:
with open(output_path, 'w+') as txtfile:
    # Initialize txt.writer
    txtfile.write(message)
    txtfile.close()