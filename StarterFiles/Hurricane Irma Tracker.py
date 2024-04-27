#Arun Agarwal Hurricane Irma Tracker

import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.
       :return: a tuple containing the Turtle and the Screen
       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)
    # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-95, 0, -17.66, 45)
    # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    with open("images/irma.csv", 'r') as oFile:
        lines = [line.strip() for line in oFile.readlines()]
        lines = lines[1:]
        lines = [line.split(',') for line in lines]
        lines = [line[2:5] for line in lines]

    t.penup()

    start = lines[0]
    yStart = start[0]
    xStart = start[1]

    xStart = float(xStart)
    yStart = float(yStart)

    t.hideturtle()

    t.setx(xStart)
    t.sety(yStart)

    elements = len(lines)
    for i in range(elements):
        update = lines[i]
        y = update[0]
        x = update[1]
        wind = update[2]
        wind = int(wind)
        x = float(x)
        y = float(y)

        if wind < 74:

            t.width(1)
            t.pencolor("white")

        elif wind >= 74 and wind <= 95:

            t.width(3)
            t.pencolor("blue")
            t.write("1", font=("Arial", 15))

        elif wind >= 96 and wind <= 110:

            t.width(5)
            t.pencolor("green")
            t.write("2", font=("Arial", 15))

        elif wind >= 110 and wind <= 129:

            t.width(7)
            t.pencolor("yellow")
            t.write("3", font=("Arial", 15))

        elif wind >= 130 and wind <= 156:

            t.width(8)
            t.pencolor("orange")
            t.write("4", font=("Arial", 15))

        elif wind >= 158:

            t.width(11)
            t.pencolor("red")
            t.write("5", font=("Arial", 15))

        i += 3
        t.showturtle()
        t.pendown()
        #t.color("black")
        t.goto(x, y)

    wn.exitonclick()

if __name__ == "__main__":
    irma()
