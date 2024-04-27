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

#Arun Agarwal, Hold-at-20 Outcomes

import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value

simulations = int(input("How many Hold-at-20 turn simulations?"))
data = {}
probability = 0.0

def simulate(y):
    for _ in range(y):
        total = 0
        x = 0
        while total < 20:
            x = roll()
            if x == 1:
                total = 0
                break
            else:
                total += x
        if total not in data:  
            data[total] = 1
        else:
            data[total] += 1
    return total
simulate(simulations)
for key in sorted(data.keys()):
    data[key] = data[key]/simulations
print("Score   Estimated Probability")
print("\n".join("{}\t{}".format(k,v) for k,v in sorted(data.items())))

#Arun Agarwal, Hold-at-X Outcomes
import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value

simulations = int(input("How many Hold-at-X turn simulations?"))
hold = int(input("What value will you hold at?"))
data = {}
def simulate(y,z):
    for _ in range(y):
        total = 0
        x = 0
        while total < z:
            x = roll()
            if x == 1:
                total = 0
                break
            else:
                total += x
        if total not in data:  
            data[total] = 1
        else:
            data[total] += 1
    return total
simulate(simulations,hold)
for key in sorted(data.keys()):
    data[key] = data[key]/simulations
print("Score   Estimated Probability")
print("\n".join("{}\t{}".format(k,v) for k,v in sorted(data.items())))

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


#Arun Agarwal, Average Pig Turns

import random
def roll():
    roll_value = random.randint(1,6)
    return roll_value

games = int(input("Games?"))

def turn(game):
    totalTurns = 0
    for _ in range(game):
        total = 0
        x = 0
        score = 0
        while score < 100:
            while total < 20: 
                x = roll()
            
                if x == 1:
                   total = 0
                   score += total
                   break
                else:
                    total += x
            totalTurns += 1
            score += total
            total = 0
            
    print("Average Turns: ", totalTurns/games)
turn(games)

#I did not get to finish programs 7 and 8 because I could not figure them out and I ran out of time
