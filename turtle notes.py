import turtle

bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(10)
bob.speed(1)
bob.turtlesize(2, 2)

for x in range(0,5):
    if x % 2 ==0:
        bob.pencolor("blue")
    else:
        bob.pencolor("red")


#for x in range(0,20):
    bob.forward(100)
    bob.penup()
    bob.forward(100+x*20)
    bob.stamp()

    #Move back to starting x coordinate
    bob.right(180)
    bob.forward(200+x*21)

    bob.left(90)
    bob.forward(20)

    bob.left(90)
    bob.pendown()
"""
for x in range(0,50):
    bob.forward(50 + 10*x)
    bob.right(147)

colors = ["red", "green", "blue"]

#for color in colors[::-1]:
 #   bob.pencolor(color)
  #  bob.forward(30)

for index, color in enumerate(colors):
    print(index, color)
    bob.pencolor(color)
    bob.forward((index+1)*50)
"""
