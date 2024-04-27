#Arun Agarwal Regex Assignment
#Program 4: Kinda a Regex Problem

import random
import re
text = open('words.txt', 'r')
for word in text:
    word = word.strip().lower()
compilation = re.compile(r'[a-z]{4,}')
four_letters_long = compilation.findall(words)
random_four_words = random.sample(four_letters_long,4)
print('Your password: ',''.join(random_four_words))
