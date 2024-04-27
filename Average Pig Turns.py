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
