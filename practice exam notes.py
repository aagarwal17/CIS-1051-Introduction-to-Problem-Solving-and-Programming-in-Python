#MONTY CARLOS PROBLEM- 20 POINTS
#randint problem with dice; a game; pig latin and pig (first three) assignments should be reviewed
# list relies on indecides, can append stuff and add it to the end; dictionaries have keys and must define keys; keys can be whatever you want, not just numbers
#3. reverses the list
#4. s[-3:] or s[len(s) - 3]

#5.how to simulate a coin flip
 	number = randint(0,1)
 	if number == 0:
		return “Heads!”
	else:
		return “Tails!”
 print(coinflip())

#Weighted coin:
random.randint(1,2)
random.choices(["H", "T"], [0.55, 0.45])
or
outcomes = ["H"]*55 + ["T"]*45
random.choice(outcomes)
or
random.randint(1,100)
if >=45, heads; if <=45, tails

#6. file reading average gpa, worstgpa, oldest student, median gpa
def gpaProblem():
    data = open("students.csv", 'r')
    total = 0
    count = 0

    worstStudent = ""
    worstGPA = 5.0


    oldestStudent = ""
    maxAge = 2

    gpas = []  
    
    for line in data:
        line = line.split(",")
        age = int(line[3])
        gpa = float(line[-1])
        gpas.append(gpa)
        
        if gpa < worstGPA:
            worstGPA = gpa
            worstStudent = line[0] + line[1]
            
        if age > maxAge:
            maxAge = age
            oldestStudent = line[0] + line[1]
            
        if age > 40:
            total += gpa
            count += 1

    print(total/count)
    sorted(gpas)
    print( gpas[len(gpas//2)])


#7. sum of evens
def evenFileSum():
    data = open("numbers.csv", 'r')
    sum = 0
    for line in data:
        line = line.split(",")
        for item in line:
            num = int(item)
            if item % 2 == 0:
                sum += item
    print(sum)

#8. add or delete a string to begining of word

def unOrUn(word):
    if word[:2] == "un":
        #remove un
        return word[2:]
    else:
        #add un
        return "un" + word

#9. biggest and smallest thing in a list and substract them

def maxMinDiff(numbers):
    return max(numbers) - min(numbers)
or
def maxMinDiff(numbers):
    biggest = numbers[0]
    smallest = numbers[0]

    for n in numbers:
        if n > biggest:
            biggest = n
        if n < smallest:
            smallest = n
    return biggest - smallest


#10. swap numbers

def swapEnds(numbers):
    first = numbers[0]
    last = numbers[-1]

    numbers[0] = last
    numbers[-1] = first

#11. for every pair, val is >= one of them
def isEverywhere(nums, val):
    for i in range(len(nums) - 1):
        left = nums[i]
        right = nums[i + 1]

        if left != val and right != val:
            return False
    return True

#12. sums numbers in a word
def sumStringDigits(word):
    total = 0
    for char in word:
        if char.isdigit():  (or you can do if char in "0123456789":)
            total += int(char)
    return total
        
#13. sums the digits
def sumDigits(num):
    total = 0
    num.remove(-)
    while num > 0:
        lastDigit = num % 10
        total += lastDigit
        num = num//10
    return total


#Monty Carlos Problem:
def headTails():
    rosen = "THH"
    student = "HHT"
    outcomes =["H", "T"]
    results = {}
    
    for i in range(100000):
        flips = ""

        while flips[-3:] != rosen and flips[-3] = student:
            flips += random.choice(outcomes)

        winner = flips[-3:]
        if winner not in results:
            results[winner] = 1
        else:
            results[winner] = results[winner] + 1
    for key in results:
        print(key, results[key]/100000)



#WildCat Problem
def hasWildCat(word):
    for index in range(len(word) - 2):
        c = word[index]
        if c == 'c' and word[index + 2] == 't': 
            return True
    return False
    

#Most common char in string
def mostCommonChars(s):
    counts = {}
    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            coutns[char] += 1
    mostCommon = ''
    mostCount = -1

    for key in counts:
        if counts[key] > mostCount:
            mostCommon = key
            mostCount = counts[key]
    return mostCommon


