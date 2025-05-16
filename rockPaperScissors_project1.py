import random

user_choice_st = input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors. ")
user_choice = int(user_choice_st)
if user_choice >= 3 or user_choice < 0:
    print("Invalid input.")
else:
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You won.")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif computer_choice > user_choice:
        print("You lose.")
    elif computer_choice < user_choice:
        print("You won.")
    else:
        print("Invalid input.")
