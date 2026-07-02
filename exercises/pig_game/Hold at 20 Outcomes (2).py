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
