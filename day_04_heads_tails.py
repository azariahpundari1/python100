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
        option = "Tails"
        print(display_outcome(user_input, option))
        
    elif random_number == 1:
        print("Heads")
        option = "Heads"
        print(display_outcome(user_input, option))


def display_outcome(user_choice, outcome):
    """Display the outcome if the player has won or lost"""
    if user_choice == outcome:
        return "You win!"
    else:
        return "You lose!"


if __name__ == "__main__":
    main()
