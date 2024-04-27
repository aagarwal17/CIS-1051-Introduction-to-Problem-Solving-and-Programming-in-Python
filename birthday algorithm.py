import random

def generateBirthday():
    return random.randrange(1,365)

def generateBirthdayList(num):
    birthdays = []

    for _ in range(num):
        birthdays.append(generateBirthday())
    return birthdays


def countPairs(birthdays):
    numPairs = 0
    for startIndex in range(len(birthdays)):
        birthday = birthdays[startIndex]
        for index in range(startIndex + 1 , len(birthdays)):
            numPairs += 1
    return numPairs


def hasDuplicateBirthday(birthdays):
    sortedList = sorted(birthdays)
    for i in range(len(sortedList) - 1):
        left = birthdays[i]
        right = birthdays[i+1]
        if right == left:
            return True, left
    return False

def checkCountsForDuplicates(counts):
    for birthday in counts:
        if count[birthday] > 1:
            return True
    return False

    """numPairs = 0
    for startIndex in range(len(birthdays)):
        birthday = birthdays[startIndex]
        for index in range(startIndex + 1 , len(birthdays)):
            otherBirthday = birthdays[index]
            if birthday == otherBirthday:
                return True, birthday
    return False"""

def countNplicates(counts):
    nplicates = {}
    for birthday in counts:
        count = counts[birthday]
        if count not in nplicates:
            nplicates[count] = 1
        else:
            nplicates[count] = nplicates[count] + 1
    return nplicates

def countBirthdays(birthdays):
    counts = {}
    for birthday in birthdays:
        if birthday not in counts:
            counts[birthday] = 1
        else:
            counts[birthday] = counts[birthday] + 1
    return counts
    
def main():
    
"""birthdays = generateBirthdayList(70)
counts = countBirthdays(birthdays)"""
    hits = 0
    for _ in range(10000):
        birthdays = generateBirthdayList(50)
        counts = ciuntBirthdays(birthdays)
        if checkCountForDuplicates(counts)
            hits += 1
            #if hasDuplicateBirthday(birthdayList):
             #   hits += 1
    print(hits, hits/100, %)


    birthdays = generateBirthdayList(50)
    counts = ciuntBirthdays(birthdays)

main()
