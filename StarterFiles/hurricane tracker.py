#Arun Agarwal Hurricane Tracker
#10/30/2019

def irma():
    text = open("images/irma.csv")
    lines = text.readlines()

    category = 0

    t, wn, map_bg_img = irma_setup()
    t.penup()

    for line in lines[1:]:
        line = line.strip().split(",")
        lat = float(line[2])
        lon = float(line[3])
        wind = float(line[4])

        if wind < 74:
            t.color("white")
            t.pensize(5)
        elif 74 <= wind <= 95:
            t.color("blue")
            t.pensize(10)
            category = 1
        elif 96 <= wind <= 110:
            t.color("green")
            t.pensize(15)
            category = 2
        elif 111 <= wind <= 129:
            t.color("yellow")
            t.pensize(20)
            category = 3
        elif 130 <= wind <= 156:
            t.color("orange")
            t.pensize(25)
            category = 4
        else:
            t.color("red")
            t.pensize(30)
            category = 5

        t.goto(lon, lat)
        t.pendown()
        t.color("black")
        t.write(category)

    wn.mainloop()
