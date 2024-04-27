#Temperature Program
#Arun Agarwal
cel = float(input("What is the temperature in Celsius?"))
far = cel * (9/5) + 32
print(cel, "degrees Celsius is", far, "degrees Farenheit")

#Seconds to Hours Program
#Arun Agarwal
seconds = int(input("Enter the number of seconds you want to convert: "))
hours = seconds//3600
minutes = (seconds % 3600)//60
print("Hour(s) = ", hours, "\nMinute(s) = ", minutes, "\nSecond(s) = ", (seconds % 3600) % 60)

#Sorting Program
#Arun Agarwal
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))
num3 = int(input("Please enter a third integer: "))

if num1 > num2:
           temp = num2
           num2 = num1
           num1 = temp
if num2 > num3:
           temp = num3
           num3 = num2
           num2 = temp
if num1 > num2:
           temp = num2
           num2 = num1
           num1 = temp

print("sorted: ", num1, num2, num3)
