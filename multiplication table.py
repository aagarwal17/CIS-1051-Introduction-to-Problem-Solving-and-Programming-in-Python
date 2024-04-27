
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

number = int(input("Choose a positive integer: "))
table(number)
