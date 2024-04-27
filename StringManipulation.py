#Arun Agarwal     10/19/2019
#String Manipulation Project

#Function 1: finds index of first vowel, if it exists, one parameter
def findFirstVowel(word):

    vowel = ["a", "e", "i", "o", "u"]

    none = -1
    for i in range(len(word)):
        if(word[i] in vowel):
            return(i)
    return(none)

    #returns index of the first vowel
    #if there is no vowel, return the index of the last character


#Function 2: turns the parameter into the Pig Latin form of the word
def convertToPigLatin(word):
    ayWord = "ay"
    wayWord = "way"

    length = len(word)
    foundVowel = findFirstVowel(word)

    if (foundVowel == -1): #there are no vowels
        mnpword = word
    elif (foundVowel == 0): #the first letter is a vowel
        firstLetter = word[0]
        mnpword = word[1:length] + firstLetter + wayWord
    else: #vowel exists and is not first letter
        firstLetter = word[0:foundVowel]
        mnpword = word[foundVowel:length] + firstLetter + ayWord
    return(mnpword)


#pig latin form of the inputted word
    # if the word starts with a vowel, move the vowel to the end of the word and additionall add"way to the end of the word
    # else (but still a vowel), move all letters before first vowel to the end fo the word and add "ay" to the end of the word


#Function 3: reverses the characters in the original string
def reverse(word):
    reversedWord = ""

    for char in word:
        reversedWord = char + reversedWord
    return(reversedWord)

    
    # if there is no vowel, return String unchanged

#Function 4: transforms word into ROT13
def rot13(word):
    first = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    second = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    one = list(word)
    length = len(one)
    new = []
    for x in one:
        if x in first:
            y = first.index(x)
            new.append(second[y])
        else:
            y = second.index(x)
            new.append(first[y])
    new = "".join(new)
    return new


#Main Function: runs Pig Latin program until user inputs done
def main():
    word = input("Input a Word to Convert. If done type 'done': ")
    word = word.lower()
    while (word != "done"):
        print("Pig Latin: " + convertToPigLatin(word))
        print("Reversed: " + reverse(word))
        print("ROT13: " + rot13(word))
        word = input("Input a Word to Convert. If done, type 'done' ")
        word = word.lower()
    return word 
main()



