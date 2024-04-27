#Arun Agarwal
#Intermediate Loop Problems


#Program 1: Number of Vowels:
def vowels(word):
    lword = word.lower()
    count = 0
    count += lword.count("a")
    count += lword.count("e")
    count += lword.count("i")
    count += lword.count("o")
    count += lword.count("u")
    return count


#Program 2: Number of Even Digits:
def even(num):
    count = 0
    while num > 0:
        remainder = num % 10
        if (remainder % 2 == 0):
            count += 1
        num = num//10
    return count



#Program 3: Three Digit Armstrong Numbers:
def armstrong(num):
    newnum = num
    sum = 0
    while newnum > 0:
        remainder = newnum % 10
        remainder = (remainder ** 3)
        sum += remainder
        newnum = newnum//10
    if (sum == num):
        return True
    


#Program 4: The Riddler:
def riddler():
    for number in range(1000,10000):
        num1 = number//1000
        number = number % 1000
        num2 = number//100
        number = number % 100
        num3 = number//10
        number = number % 10
        num4 = number

        if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num3 and num2 != num4 and num3 != num4:
            if(num1 == 3* num2):
                if num4 % 2 != 0:
                    if num1 + num2 + num3 + num4 == 27:
                        return "The Address is " + str(num1) + str(num2) + str(num3) + str(num4) + " Pennsylvania Avenue."
        

#main program starts here

print("Program 1: Number of Vowels:")
word = input("Please Type a Word: ")
print(vowels(word))

print("Program 2: Number of Even Digits:")
num = int(input("Please Type a Number: "))
print(even(num))

print("Program 3: Three Digit Armstrong Numbers:")
num = int(input("Please Type a Number: "))
if(armstrong(num)):
    print(num, "is an armstrong number." )
else:
    print(num, "is not an armstrong number.")
                    
print("Program 4: The Riddler")
print(riddler())
