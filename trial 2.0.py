import random
import re

text = open('words.txt', 'r')
for word in text.readlines():
    word.strip().lower()
compilation = re.compile(r'[a-z]{4,}')
four_letter_longs = compilation.findall(text)
random_four_words = random.sample(four_letters_longs,4)
print('Your password: ',''.join(random_four_words))
