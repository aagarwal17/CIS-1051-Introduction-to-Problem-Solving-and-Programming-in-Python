#Arun Agarwal
#Blame the Pope Program

def isLeapYear(year):
    if(year % 4 == 0):
                    if year % 100 == 0 and not (year % 400 == 0):
                        return False
                    else:
                        return True 
    else:
        return False
    
date = input("Please enter a date (MM/DD/YYYY): ")
month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:]

                  
if (month > 12 or month < 1):
    print("Invalid Month.")
else:
    if (month == 4 or month == 6 or month == 9 or month == 11):
        if (day < 1 or day > 30):
            print("Invalid Day for this Month.")
        else:
            print("Valid Date.")
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8  or month == 10 or month == 12):
        if (day < 1 or day > 31):
            print("Invalid Day for this Month.")
        else:
            print("Valid Date.")
    else (month == 2):
            if (1 <= day <= 28):
                print("Valid Date.")
            elif day = 29 and isLeapYear(year):
                print("Valid Date.")
            else:
                print("Invalid Day for this Month.")
    
          
