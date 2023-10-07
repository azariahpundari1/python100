import random

# Display question
print("Heads or Tails?")

# Get user input
user_input = input(">>> ").capitalize()

# Get random number between 0 & 1
random_number = random.randint(0,1)
if random_number == 0:
    print("Tails")
    if user_input == "Tails":
        print("You win!")
    else:
        print("You lose :(")
elif random_number == 1:
    print("Heads")
    if user_input == "Heads":
        print("You win!")
    else:
        print("You lose :(")

#TODO create functions for concisness
