#Arun Agarwal, Hold-at-20 or Goal Turn

import random
score = int(input("Score? "))

def roll():
    roll_value = random.randint(1,6)
    return roll_value

def turn():
    total = 0
    x = 0
    s = score
    while total < 20 and s < 100:
        x = roll()
        print("Roll: " + str(x))
        if x == 1:
            total = 0
            break
        else:
            total += x
        s += x
    print("Turn Total: " + str(total))
    print("New Score: " + str(s))
    
turn()
