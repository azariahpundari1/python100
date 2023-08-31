"""
Tip calculator program
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

Write your code below this line 👇
"""

# Display welcome message
print("Welcome to the tip calculator")

# Get bill
total_bill = float(input("What was the total bill? $"))

# Get percentage for tip
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_decimal = (tip_percentage / 100) + 1
# Get number of people
num_of_people = int(input("How many people to split the bill? "))

# Calculate tip
total_tip = ((total_bill * tip_percentage / 100) + total_bill) / num_of_people
print(f"Each person should pay ${round(total_tip, 2)}")