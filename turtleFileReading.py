import turtle

commands = open("turtle boss.commands.py", 'r')
bob = turtle.Turtle()

for line in commands:
    parts = line.split()
    command = parts[0]
    amount = int(parts[1])
    if command == "f":
        bob.forward(amount)
    if command == "r":
        bob.right(amount)
    if command == "l":
        bob.left(amount)
