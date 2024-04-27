#Arun Agarwal, One Automated Turn of Pig
import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value

def turn():
    total = 0
    x = 0
    while total < 20:
        x = roll()
        if x == 1:
            print("Roll: " + str(x))
            total = 0
            print("Turn Total: " + str(total))
            return total
        print("Roll: " + str(x))
        total += x
    print("Turn Total: " + str(total))
    return total
def play():
    score_1 = 0
    score_2 = 0
    while score_1 < 100 or score_2 < 100:
        score_1 += turn()
        print("Player 1 Score: " + str(score_1))
        if score_1 >= 100:
            break
        score_2 += turn()
        print("Player 2 Score: " + str(score_2))
        if score_2 >= 100:
            break
    if score_1 > score_2:
        print("Winner is Player 1!")
        return score_1
    else:
        print("Winner is Player 2!")
        return score_2

print("Winning Score: " + str(play()))
