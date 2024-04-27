import random

def rollDice(numDice=1, sides =6):
    total = 0
    for _ in range(numDice):
        total = total + random.randint(1, sides)
    return total

def roll4d6DropLowest():
    rolls = []
    for _ in range(4):
        rolls.append(rollDice())
        return sum(rolls) - min(rolls)

def roll5d6DropLowest2():
    rolls = []
    for _ in range(4):
        rolls.append(rollDice())
        return sum(sorted(rolls)[2:]


def calcHits():
    #1d20 + 5
    hits = 0
    targetAC = 15
    for _ in range(10000):
        roll = rollDice(1,20) + 5
        if role >= targetAC:
        hits += 1
    print(hits/100000)

def cakcKillGoblin():
    trials = 100000
    targetAC = 15
    results = {}
    for _ in range(trials):
        roll = rollDice(1,20) + 5
        damage = 0
        if role >= targetAC:
            damage = rollDice(2,6) + 3

        if damage not in results:
            results[damage] = 1
        else:
            results[damage] = results[damage] + 1
    return results
""" 
def main():
    stats = {}
    for _ in range(10000):
        roll = roll4d6DropLowest()
"""

def main():
    results = calcKillGoblin()
    for damage in sorted(results.keys()):
        print(damage,results[damage]/100000)

calcHits()
        
