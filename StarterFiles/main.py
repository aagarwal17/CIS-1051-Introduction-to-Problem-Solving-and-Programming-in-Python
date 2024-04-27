#Arun Agarwal Hurricane Tracker
#10/30/2019

import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.
       Returns a tuple containing the Turtle and the Screen
    """
    
    import tkinter
    turtle.setup(965, 600)
    # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)
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
    data = open("irma.csv", 'r')
    for line in data:
        parts = line.split()
        latitude = parts[2]
        longitude = parts[3]

if __name__ == "__hurricane tracker__":
    irma()


