#Create a program that takes a user's age as input and outputs the year in which they will turn 100 years old. Assume that the user enters a valid positive integer as their age.

import datetime
#What is your name
name = input("what is your name: ")

# Get the user's age as input
age = int(input("What is your age? "))

# Calculate the year in which the user will turn 100
current_year = datetime.datetime.now().year
year_of_100 = current_year + (100 - age)

# Output the result
print(name + " You will turn 100 in the year", year_of_100)


