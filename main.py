import random

user_wins = 0
comp_wins = 0
draw = 0
options = ["rock", "paper", "scissors"]

print("-------Rock paper scissors-------\n")
print("1.rock\n2.scissors\n3.paper\n4.e to Exit\n")
print("NOTE: Please Type in lowercase...")

while True:
    user_choice = input("Type your choice: ").lower()
    if user_choice == 'e':
        print("User Wins:", user_wins)
        print("Computer Wins:", comp_wins)
        print("Draw:", draw)
        quit()

    # validating user input
    if user_choice not in options:
        continue

    random_number = random.randint(0, 2)
    comp_choice = options[random_number]
    print("Computer chose", comp_choice)
    if user_choice == "rock" and comp_choice == "scissors":
        print("User wins!")
        user_wins += 1
        continue
    elif user_choice == "scissors" and comp_choice == "paper":
        print("User wins!")
        user_wins += 1
    elif user_choice == "paper" and comp_choice == "rock":
        print("User wins!")
        user_wins += 1
    elif user_choice == comp_choice:
        print("It's a Draw!")
        draw += 1
    else:
        print("Computer wins!")
        comp_wins += 1
        continue
