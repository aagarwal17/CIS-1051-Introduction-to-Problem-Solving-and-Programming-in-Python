#This program will not work because you have not downloaded Cimage (a add-on) to your laptop

import image

win = image.ImageWin(640,480, "Image Processing")
myPic = image.EmptyImage(100,100)

redPixel = image.Pixel(255,0,0)
#for i in range(100):
#    myPic.setPixel(i,i,redPixel)

for x in range(myPic.getWidth()):
    for y in range(myPic.getHeight()):
        myPic.setPixel(x,y, image.Pixel(0,255,0)


#myPic.draw(win)
#wn.exit_on_click()

