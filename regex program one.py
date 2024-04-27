#1. number of words with cat or dog in them:

import re

compilation = re.compile(r'cat|dog')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for goodWord in compilation.findall(line_word):
        count += 1
print("The number of words with cat or dog in them is", count)


#2. number of four letter words:

compilation = re.compile(r'^[a-z]{4}$')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for goodWord in compilation.findall(line_word):
        count += 1
print("The number of four letter words is", count)


#3. number of words with hun in them:


compilation = re.compile(r'hun')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for goodWord in compilation.findall(line_word):
        count += 1
print("The number of words with hun in them is", count)


#4. more words that end in "ing" or "ion":


compilationING = re.compile(r'ing$')
compilationION = re.compile(r'ion$')
text = open('words.txt', 'r')

countING = 0
countION = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for goodWord in compilationING.findall(line_word):
            countING += 1
    for goodWord in compilationION.findall(line_word):
            countION += 1
print("ing words:", countING, "ion words:", countION)
if (countING > countION):
    print("There are more words that end in 'ing'")
else:
    print("There are more words that end in 'ion'")
    


    
#5. count number of words that have Q or q not followed by U or u

compilation = re.compile(r'q([^u]|$)')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for goodWord in compilation.findall(line_word):
        count += 1
print("The number of words that have Q or q not followed by U or u is", count)


#6. count number of words with no vowels

compilation = re.compile(r'^[^aeiou]+$')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for match in compilation.findall(line_word):
        count += 1
print("The number of words with no vowels is", count)

#7. consist of only vowels

compilation = re.compile(r'^[aeiou]+$')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for match in compilation.findall(line_word):
        count += 1
print("The number of words with only vowels is", count)


#8. words with 'nt:

compilation = re.compile(r' n\'t')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for match in compilation.findall(line_word):
        count += 1
print("The number of words with n't is", count)


#9. words with two vowels in a row:
compilation = re.compile(r'[a-z]*[aeiou][aeiou]')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for match in compilation.findall(line_word):
        count += 1
print("The number of words with two vowels in a row is", count)

#10. words with two vowels at any place in the word:
compilation = re.compile(r'^[a-z]*[aeiou][a-z]*[aeiou][a-z]*$')
text = open('words.txt', 'r')

count = 0

for line_word in text:
    line_word = line_word.strip().lower()
    for match in compilation.findall(line_word):
        count += 1
print("The number of words with two vowels at any place in the word is", count)

#1,3, 5, 10
