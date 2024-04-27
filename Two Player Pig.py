#Arun Agarwal, Two-Player Pig

import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value

def turn(start_score):
    x = 0
    turn_total = 0
    while turn_total < 20 and start_score < 100:    
        x = roll()
        print("Roll: " + str(x))
        if x == 1:
            x = 0
            start_score -= turn_total
            turn_total = 0
        else:
            turn_total += x
            start_score += x
        if x == 0:
            break
    print("Turn Total: " + str(turn_total))
    print("New Score: " + str(start_score))
    turn_total = 0
    return start_score
    
player1 = 0
player2 = 0
while player1 < 100 and player2 < 100:
    print("It is player 1's turn")
    player1 = turn(player1)
    if player1 >= 100:
        break
    print("It is player 2's turn")
    player2 = turn(player2)
