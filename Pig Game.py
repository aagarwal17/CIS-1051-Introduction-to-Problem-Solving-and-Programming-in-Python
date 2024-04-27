#Arun Agarwal, Pig Game

import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value
def user_turn(user_score):
    turn_total = 0
    entry = ""
    x = 0
    while entry == "" and x != 1:
        x = roll()
        print("Roll: " + str(x))
        if x == 1:
            turn_total = 0
        else:
            turn_total += x
        if user_score >= 100:
            break
        elif x == 1:
            break
        else:
            entry = input("Turn Total: " + str(turn_total) + "  Roll/Hold? (Enter)")
        if entry != "":
            break
    user_score += turn_total
    print("Turn Total: " + str(turn_total))
    print("New Score: " + str(user_score))
    return user_score             
def computer_turn(computer_score):
    turn_total = 0
    x = 0
    while x !=1 and turn_total < 20:
        x = roll()
        print("Roll: " + str(x))
        if x == 1:
            turn_total = 0
        else:
            turn_total += x
        computer_score += x
        if computer_score >= 100:
            break
        elif x == 1:
            break
    print("Turn Total: " + str(turn_total))
    print("New Score: " + str(computer_score))
    return computer_score
user = random.randint(1,2)
computer = 0
print("You will be player# " + str(user))
print("Enter nothing to roll, enter anything to hold")

if user == 1: #User is Player 1
    user = 0
    while user < 100 and computer < 100:
        print("It is Player 1's Turn")
        print("Player 1 Score: " + str(user))
        print("Player 2 Score: " + str(computer))
        user = user_turn(user)
        if user >= 100:
            break
        print("It is Player 2's Turn")
        print("Player 1 Score: " + str(user))
        print("Player 2 Score: " + str(computer))
        computer = computer_turn(computer)
else: #Computer is Player 1
    user = 0
    while user < 100 and computer < 100:
        print("It is Player 1's Turn")
        print("Player 1 Score: " + str(computer))
        print("Player 2 Score: " + str(user))
        computer = computer_turn(computer)
        if computer >= 100:
            break
        print("It is Player 2's Turn")
        print("Player 1 Score: " + str(computer))
        print("Player 2 Score: " + str(user))
        user = user_turn(user)
