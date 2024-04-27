import random

def rollDice(numDice, sides):
    total = 0
    for _ in range(numDice):
        total += random.randrange(1,sides)

    return total

print(rollDice(1,8))
