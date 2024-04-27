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
