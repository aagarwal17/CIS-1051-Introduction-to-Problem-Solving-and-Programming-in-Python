#Arun Agarwal,Hold-at-20 or Goal Game
import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value

def turn():
    total = 0
    x = 0
    score = 0
    while score < 100:
        while total < 20: 
            x = roll()
            print("Roll: " + str(x))
            if x == 1:
               total = 0
               score += total
               print("Turn Total: " + str(total))
               print("New Score: " + str(score))
               break
            else:
                total += x
        score += total
        total = 0
        print("Turn Total: " + str(total))
        print("New Score: " + str(score))            
turn()
