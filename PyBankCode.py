import os
import csv

# Path to collect data from the "Downloads" folder
budget_data = os.path.join("Downloads", "budget_data.csv")

# Set variables for each value and set equal to zero (0)
total_months = 0
total_amount = 0
profit = 0

# Create lists for calculations
months = []
profit_change_list = []
grts_decr = ["", 99999999999]
grts_incr = ["", 0]

# Read CSV file
with open(budget_data) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    # Calculations
    for row in reader:
        total_months = total_months + 1
        total_amount = total_amount + int(row["Profit/Losses"])
        
        prof_change = int(row["Profit/Losses"]) - profit
        profit = int(row["Profit/Losses"])
        
        profit_change_list = profit_change_list + [prof_change]
        months = months + [row["Date"]]
        
        # Calculate greatest increase
        if (prof_change > grts_incr[1]):
            grts_incr[1] = prof_change
            grts_incr[0] = row["Date"]
            
        # Calculate greatest decrese
        if (prof_change < grts_decr[1]):
            grts_decr[1] = prof_change
            grts_decr[0] = row["Date"]
            
# Calculate profit average change
avg_change = sum(profit_change_list) / len(profit_change_list)

# Create output for print on Summary Table and export as txt file
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Amount: ${total_amount}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {grts_incr[0]} (${grts_incr[1]})\n"
    f"Greatest Decrease in Profits: {grts_decr[0]} (${grts_decr[1]})\n")
 
print(output)

text_path = os.path.join("Downloads", "data_output.txt")
with open(text_path, "w") as text_file:
            text_file.write(output)