#This program will not work because you have not downloaded C-Image (an add-on) to this PC
import image

pika = image.Image("pikachu.jpg")

win = image.ImageWin(pika.getWidth(),pika.getHeight(), "shock")




for x in range(pika.getWidth()):
    for y in range(pika.getHeight()):
        orig = pika.getPixel(x,y)
        pika.setPixel(x,y,image.Pixel(0, orig.getGreen(), orig.getBlue()))
        
pika.draw(win)
win.exit_on_click()
