#Arun Agarwal Regex Assignment
#Program 4: Kinda a Regex Problem

import random
import re





text = open('words.txt', 'r')
#lines = text.readlines()
for lines in text:
    word = lines.strip()
    
def read_file(filename):
    with open(filename,'r') as infile:
        return [word.strip() for word in infile.readlines()]

def main():
    words = read_file('words.txt')
    four_letters_longs=[word.lower() for word in words if len(word)>=4 and word.islower()]
    random_four_words = random.sample(four_letters_longs,4)
    print('Your password: ',''.join(random_four_words))

main()

#read file and store in variable
#for each word, word.strip() and word.lower()
#for each word, if length is greater than four, use findall to add to list; findall will equal a variable
#random_four_words = random.sample(variable_for_finall, 4)
#print(('Your password: ',''.join(random_four_words))
