import re

def findSupers(filename):
    text = open(filename, 'r')
    supers = []
    superRegex = re.compile(r'\w+man|\w+woman|\w+boy|\w+girl')
    for line in text:
        supers+= superRegex.findall(line)
    return supers

print(findSupers("heroes.txt"))

#know difference between match and search
#two regex problems: given a file with a bunch of social security numbers, replace all them with REDACTED, the second one will also be bubbling in
#there will be nested lists



def euler5():
    done = False
    num = 2520
    while not done:
        good = True
        for i in range(2,21):
            if num % i != 0:
                good = False
                break 
        if good:
            done = True
        else:
            num += 1
    return num

print euler5()


def sumDigits(num):
    total = 0
    while num != 0:
        total += num % 10
        num = num//10
    return total



def isPalindrome(word):
    return word == word[::-1]


#OR

def isPalindrome(word):
    reversedWord = ""
    for letter in word:
        reversedWord = letter + reversedWord

    return reversedWord == word



def makeUsername(name,n):
    initials = ""
    name = name.split(" ")
    for part in name:
        firstLetter = part[0]
        firstLetter = firstLetter.lower()
        initials += firstLetter
    return initials + str(n)



def isPermutation(word1, word2):
    count1 = {} #keys are each character in word 1
    # value is the counts of each character in word2
    count2 = {} # same, but word2

    for letter in word1:
        if letter not in count1:
            count1[letter] = 1
        else:
            count1[letter] = count1[letter] + 1



    # same, but for word2 and count2
    for letter in word2:
        if letter not in count2:
            count2[letter] = 1
        else:
            count2[letter] = count2[letter] + 1

    return count1 == count2


def belowAverage(numbers):
    avg = sum(numbers)/len(numbers)
    below = []
    for n in numbers:
        if n < avg:
            below.append(n)

    return below




def sumOfTens(numbers):
    total = 0
    for innerList in numbers:
        for item in innerList:
            in num % 10 == 0:
                total += num
    return total


def sumOfFile(filename):
    text = open(filename, 'r')
    total = 0
    for line in text:
        line = line.split(",")
        for item in line:
            total = total + int(item)
    return total
            
