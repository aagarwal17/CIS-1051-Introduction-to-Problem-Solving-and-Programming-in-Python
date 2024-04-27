number = int(input("Choose a positive integer: "))

def printbeer(number):
    for i in range(0, number, -1):
        print(number, "bottles of beer on the wall,", number, "bottles of beer.")
        print("Take one down, pass it around,", number, "bottles of beer on the wall!")
        #number -= 1
printbeer(number)
