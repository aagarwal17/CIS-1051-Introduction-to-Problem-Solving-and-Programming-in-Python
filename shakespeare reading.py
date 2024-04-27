data = open("shakespeare.txt", 'r')
text = data.readlines()
count = {}
"""
count["luck"] = 0
count["happy"] = 0
count["few"] = 0
"""
for line in text:
    for char in text:
        if char not in count:
            count[char] = 1
        else:
          count[char] = count[char] + 1
"""
for line in text:
    word = word.lower()
    word = word.strip(",")
    words = line.split(" ")
    print(words)
    for word in words:
        if word in count:
            count[word] = count[word] + 1
"""
print(count)
