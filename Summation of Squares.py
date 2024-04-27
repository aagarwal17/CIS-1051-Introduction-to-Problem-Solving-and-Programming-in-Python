number = int(input("Choose an integer: "))

def summation(number):
    sum = 0
    for i in range(number+1):
        sum += (i*i)
    print("The square of the numbers from 1 to", number, "is", sum)    

summation(number)
