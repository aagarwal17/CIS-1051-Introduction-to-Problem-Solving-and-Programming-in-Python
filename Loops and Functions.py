#Arun Agarwal
#Loops and Functions

#1: Bottles of Beer:

def printbeer(number):
    
    for i in range(number):
        print(number, "bottles of beer on the wall,", number, "bottles of beer.")
        print("Take one down, pass it around,", number, "bottles of beer on the wall!")
        number -= 1

#2: Multiplication Table:
        
def table(number):
    
    for row in range(1, number+1):
        for col in range(1, number+1):
            if(row*col < 10):
                print(row*col, end = "   ")
            elif(row*col < 100):
                print(row*col, end = "  ")
            else:
                print(row*col, end = " ")
        print()

#3: Summation of Squares:

def summation(number):
    
    sum = 0
    for i in range(number+1):
        sum += (i*i)
    print("The sum of the square of the numbers from 1 to", number, "is", sum)

#4: Hourglass:

def hourglass():
    
    for x in range(3):
        if (x==0):
            print("|"+"\"" * (10)+"|")
        elif (x==1):
            for i in range(4):
                print(" " * (i + 1), end = '')
                print("\\", end = '')
                for y in range(4 - i):
                    print(":" * (2), end = '')
                print("/")
            print("     ||     ")
            for i in range(4):
                print(" " * (4-i), end = '')
                print("/", end = '')
                for z in range(i+1):
                    print(":" * (2), end = '')
                print("\\")
        else:
            print("|"+"\"" * (10)+"|")

#5: Slash Figure:

def slashfigure(n):
    i = 4*(n-1)+2

    for row in range(n):
        for y in range(i):
            if (y < row*2):
                print("\\",end="")
            elif (y >= i-row*2):
                print("/",end="")
            else:
                print("!",end="")
        print()

#Main Program:

print("Bottles of Beer Program: ")        
number = int(input("Choose a positive integer: "))
printbeer(number)

print("Multiplication Table Program")
number = int(input("Choose a positive integer: "))
table(number)

print("Summation of Squares Program: ")
number = int(input("Choose an integer: "))
summation(number)

print("Hourglass Program: ")
hourglass()

print("Slash Figure Program: ")
n = int(input("Please enter value for n: "))
slashfigure(n)
