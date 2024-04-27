#Arun Agarwal 11/6/2019
#Introduction to Python: Hawaiian Pronunciation:

# isValidWord function
def isValidWord(validchars, word):

    for ch in word:
        ch = ch.lower()
        if validchars.count(ch) == 0:
            print(ch, "is not a valid hawaiian character")
            return False
    return True

#getHawaiianWord function
def getHawaiianWord(word):
    result = ""
    i = 0

    while i < len(word) - 1:
        ch = word[i]
        ch = ch.lower()

        if ch =='a':
            nextCh = word[i + 1]
            nextCh = nextCh.lower()

            if nextCh == 'i' or nextCh == 'e':
                result = result + "eye-"
                i = i + 1
            elif nextCh == 'o' or nextCh == 'u':
                result = result + "ow-"
                i = i + 1
            else:
                result = result + "ah-"
        elif ch == 'e':
            nextCh = word[i + 1]
            nextCh = nextCh.lower()

            if nextCh == 'i':
                result = result + "ay-"
                i = i + 1
            elif nextCh == 'u':
                result = result + "eh-oo-"
                i = i + 1
            else:
                result = result + "eh-"

        elif ch == 'i':
            nextCh = word[i + 1]
            nextCh = nextCh.lower()

            if nextCh == 'u':
                result = result + "ew-"
                i = i + 1
            else:
                result = result + "ee-"

        elif ch == 'o':
            nextCh = word[i + 1]
            nextCh = nextCh.lower()

            if nextCh == 'i':
                result = result + "oy-"
                i = i + 1
            elif nextCh == 'u':
                result = result + "ow-"
                i = i + 1
            else:
                result = result + "oh-"

        elif ch == 'u':
            nextCh = word[i + 1]
            nextCh = nextCh.lower()

            if nextCh == 'i':
                result = result + "ooey-"
                i = i + 1
            else:
                result = result + "oo-"

        elif ch == ' ' and result[len(result) -1] == '-':
            result = result[0:len(result) - 1] + " "
            
        elif ch == '\'' and result[len(result) -1] == '-':
            result = result[0:len(result) - 1] + "'"

        else:
            result = result + ch

        i = i + 1

    if i < len(word):
        ch = word[len(word) - 1]
        ch = ch.lower()

        if ch == 'a' or ch == 'e' or ch == 'o':
            result = result + ch + "h"
        elif ch == 'i':
            result = result + "ee"
        elif ch == 'u':
            result = result + "oo"
        else:
            result = result + ch

    if result[len(result) - 1] == '-':
        result = result[0:len(result) - 1]

    result = result.capitalize()
    return result


#Main Function:

def main():

    validchars = ['a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w', '\'', ' ']

    while True:
        word = input("Please enter a hawaiian word to pronounce: ")
        word = word.strip()

        if(isValidWord(validchars, word)):
            result = getHawaiianWord(word)

            word = word.upper()
            print(word, "is pronounced", result)

        choice = input("\nDo you want to enter another word? Yes/Y or No/N: ")
        choice = choice.upper()

        while choice != "YES" and choice != "Y" and choice != "NO" and choice != "N":
            print("Please enter Yes/Y or No/N: ")
            choice = input("Do you want to enter another word? Yes/Y or No/N: ")
            choice = choice.upper()

        if choice != "YES" and choice != "Y":
            break

main()
        


















        


















            
