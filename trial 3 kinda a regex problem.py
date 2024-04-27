#Arun Agarwal Regex Assignment
#Program 4: Kinda a Regex Problem

import random
import re

def wordPassword():
    compilation = re.compile(r'^[a-z]{4,}$')
    text = open('words.txt', 'r')#.readlines()

    words = []

    for line_word in text:
        line_word = line_word.strip().lower()
        for goodWord in compilation.findall(line_word):
            words.append(goodWord)
    random_four_words = random.sample(words,4)
    print('Your password: ',''.join(random_four_words))
        
wordPassword()

#I was not sure if I had to include all words or just words that have only lower
#case letters, so the program above makes all words lower case, and the one below
#only makes a password out of lower case words

"""
import random
import re

def wordPassword():
    compilation = re.compile(r'^[a-z]{4,}$')
    text = open('words.txt', 'r')#.readlines()

    words = []

    for line_word in text:
        line_word = line_word.strip()
        for goodWord in compilation.findall(line_word):
            words.append(goodWord)
    random_four_words = random.sample(words,4)
    print('Your password: ',''.join(random_four_words))
        
wordPassword()
"""
