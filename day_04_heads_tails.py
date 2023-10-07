import random

# Display question
print("Heads or Tails?")

# Get user input
user_input = input(">>> ")

# Get random number between 0 & 1
random_number = random.randint(0,1)
if random_number == 0:
    print("Tails")
elif random_number == 1:
    print("Heads")

