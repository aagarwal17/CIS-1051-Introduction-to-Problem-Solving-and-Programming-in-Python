file = open("dictionary.txt",'r')

#printing all words in file
"""
for line in file:
    line = line.strip()
    print(line)
print("done")


#counting number of words in file
count = 0
for line in file:
    count +=1
print(count)
"""

ing = 0
ion = 0
for line in file:
    line = line.strip()
    if line[-3:] == "ING":
        ing+=1
    if line[-3:] == "ION":
        ion+=1
print(ing, ion)
