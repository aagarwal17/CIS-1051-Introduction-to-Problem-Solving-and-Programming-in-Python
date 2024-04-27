text = open("Pokemon.csv", 'r')


toughest = ""
strongest = ""
bestHP = -1
bestATK = -1

best = ""
bestStats = -1

for line in text:
    line = line.strip()
    line = line.split(",")
    if line[0] == "#" or bool(line[-1]) == "True":
        continue
    name = line[1]
    hp = int(line[5])
    atk = int(line[6])
    dfn = int(line[7])
    spa = int(line[8])
    sdf = int(line[9])
    spd = int(line[10])
    total = hp + atk + dfn + spa +spd + sdf
    avg =  total/6

    if avg > bestStats:
        
    
    if hp > bestHP:
        bestHP = hp
        toughest = name
    if atk > bestATK:
        bestATK = atk
        strongest = name
    print(toughest, bestHP)
    print(strongest, bestATK)
