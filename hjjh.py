def printDiagonal(s):
    letters = s.split()
    for row in range(len(s)):
        print(" " * row, letters[row])
          
printDiagonal("Hello")
