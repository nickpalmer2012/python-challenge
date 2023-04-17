#Import os module
import os
#implement csv module for reading the election data csv file
import csv

#define global variables
total_votes = 0
candidate = []
cand_list = []
#set starting vote count for each candidate
stockham_vote = 0
#set candidate votes as dictionary
cand_votes = {}




#Store the file path associated with the election data csv file
elect_path = os.path.join('Resources/election_data.csv')

with open(elect_path) as elect_file:
    
    #specify delimeter in election data csv file, should be comma
    #set variable for reading of election data file, elect_reader
    elect_reader = csv.reader(elect_file, delimiter=',')
    
    #calculate total number of votes cast
    
    #skip the first line from the count as the first row is headers
    next(elect_reader)
    
    #set up for loop to count total votes and create list of all candidates that received votes
    for row in elect_reader:
        total_votes = total_votes + 1
        #create variable that fetches the candidate column of the dataset
        candidate = row[2]

        #if statement to create list of the candidates that received votes
        if candidate not in cand_list:
            cand_list.append(candidate)
            #add candidate names list to cand_votes dictionary and set the candidate's starting tally to 0; Keys are cadidate names, values are count of votes
            cand_votes[candidate] = 0
        

        cand_votes[candidate] = cand_votes[candidate] + 1

    #calculate percentage of total votes for each candidate
    percentage = {}
    for i in cand_votes:
       vpercent = round(cand_votes[i]/total_votes * 100, 3)
       percentage[i] = vpercent
       #print(percentage)
       #print(cand_votes[i])

    win = max(cand_votes, key=cand_votes.get)

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")   
    #for cand_result in cand_list:
     #   print(cand_result)
    for j in range(0, len(cand_list)):
        print(cand_list[j] + ": " + str(percentage[cand_list[j]]) + "% (" + str(cand_votes[cand_list[j]]) + ")")
    print("----------------------------") 
    print(f"Winner: {win}")
    print("----------------------------")

        
       


   
















