# python-challenge
## PyBank Challenge

This was the most challenging section of the script for this problem:
![image](https://user-images.githubusercontent.com/128104435/232923503-59fce934-0a57-489f-b169-060d74f62c5f.png)
I set up a for loop to iterate through all of the rows in the given .csv file. 
I isolated the profit numbers in the data set to a list by setting the profit variable equal to the "row" that was being evaluated in the loop and 
selecting the index [1] for the profit column. 

The total profit was calculated by using the += operator, so that the profit number for each row in the for loop would be added to a running total named "total"

In order to get the profit changes over the entire dataset, I created a list of changes.  

The difficult part here was eliminating the first profit from January 2016 from the list of changes.

My friend, who works as an automation specialist in Denver recomended that I set an if statement that will append the change calculations to the change list ONLY if the prior profit does not equal 0.  The prior profit variable was initialized as 0, so this if statement effectively removed the first month's profit from the change list.  





##  PyPoll Challenge
I had to search the web to find a solution to creating a list of candidates after looping through all of the rows in the csv file, and add votes to each candidate's name in a dictionary. 



my solution came from the answer to this question in stackoverflow: https://stackoverflow.com/questions/65541642/how-do-i-loop-through-a-csv-file-and-create-a-list-based-on-the-values-in-the-li

This is the code in my script: 
![image](https://user-images.githubusercontent.com/128104435/232338904-f0980978-8442-4b82-8e63-e59885c10e96.png)

I utilized dictionaries to attach the percentage vote and total votes that needed to be paired to each candidate that received a vote in the election.

To determine the winner, I found out how to get the max value from a dictionary and return the corresponding key for that max value. I found code that was solving a similar problem from this website: https://datagy.io/python-get-dictionary-key-with-max-value/

## Print Statements
I was able to figure out most of the syntax for exporting the results to a .txt file from this website: https://www.pythontutorial.net/python-basics/python-write-text-file/
