import os
import csv

bank_data = os.path.join('Resources/budget_data.csv')

with open(bank_data) as bank_file:
    #Set bank_reader as the reading of budget data csv with a comma as the delimiter
    bank_reader = csv.reader(bank_file,delimiter = ',')
    #adjust bank_reader to read data after header row
    next(bank_reader)
    #create list that has pairs of data that show the profit/loss number next to the corresponding month
    data = list(bank_reader)
    
    #calculate number of months evaluated in data set
    num_months = len(data)
    #print(num_months)
    
    #Calculate total profit/loss over dataset
    #initialize total variable to 0
    total = 0
    prior_profit = 0
    total_change = 0
    changes = 0
    change_list = []

    #loop through each row and add profit/loss to running total variable
    for row in data:
        #month = row[0]
        profit = int(row[1])
        total += profit
        
        changes = profit - prior_profit
        #ignore any month were the prior profit = 0, else add change to change_list
        if prior_profit is not 0:
            change_list.append(changes)
        
        total_change += changes


        prior_profit = profit

    avg_change = sum(change_list)/len(change_list)
    #max change
    maxChange = max(change_list)
    #max change position on dataset
    maxChange_position = change_list.index(maxChange)+1
    #min change
    minChange = min(change_list)
    #min change position on dataset
    minChange_position = change_list.index(minChange)
    




        


    
    #print(data)


#print(num2)
print(f"Total: ${total:,}")
print(num_months)
print(maxChange)
print(minChange)
print()


#print(avg_change)
#print(maxChange_position)



