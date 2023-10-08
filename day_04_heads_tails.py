import random

def main():
    # Display question
    print("Heads or Tails?")

    # Get user input
    user_input = input(">>> ").capitalize()

    # Get random number between 0 & 1
    random_number = random.randint(0,1)
    if random_number == 0:
        print("Tails")
        if user_input == "Tails":
            print("You win!":
        else:
            print("You lose :(")
    elif random_number == 1:
        print("Heads")
        if user_input == "Heads":
            print("You win!")
        else:
            print("You lose :(")


#TODO Create functions for concisness
def display_outcome(choice, option):
    """Display the outcome if the player has won or lost"""
    if choice == option:
        return "You win!"
    else:
        return "You lose!"


if __name__ == "__main__":
    main()
