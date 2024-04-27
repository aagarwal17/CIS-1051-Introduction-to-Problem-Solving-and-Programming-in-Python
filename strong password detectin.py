#Arun Agarwal Regex Assignment
#Program 3: Strong Password Detection

import re
print('Please type a strong password: ')
password = input()

def strongPassword(password):
    compilation = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).{8,}$')
    passes = compilation.search(password)
    if passes:
        return True
    else:
        return False

if strongPassword(password) == True:
    print("Strong Password")
else:
    print("This is not a strong password")


"""
    if space_length.search(password) == None:
        #print('The entered password should have at least 8 characters and no space in between')
    if digit.search(password) == None:
        #print('The entered password doesn\'t have a digit')
  
    if lowercase.search(password) == None:
        #print('The entered password doesn\'t have a lower case character')
   
    if uppercase.search(password) == None:
        #print('The entered password doesn\'t have an upper case character')
    else:
        return True

space_length = re.compile(r'\w{8,}')
digit = re.compile(r'\d+')
lowercase = re.compile(r'[a-z]')
uppercase = re.compile(r'[A-Z]')"""
