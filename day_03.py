"""
Day 3 project: Treasure Island
This is a basic project using conditional statements
"""

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("Left or Right? ").casefold()
if direction == "Left":
    # print("test")
    action = input("Swim or Wait? ").casefold()
else:
    print("Game Over.")


door = input("Red, Blue or Yellow? ").casefold()


