from graphicalObjects import *


def patch2(win, colour, tlOffset):
    for y in range(0,100,10):
        x = 90-y
        x = tlOffset.getX() + x
        y = tlOffset.getY() + y
        rectangle(win, Point(x,y), Point(x+10,y+10), colour)


################################################################

def patch1(win, colour, tlOffset):
    altColour = True
    
    tl = Point(tlOffset.getX() + 50, tlOffset.getY() + 25)
    tl2 = Point(tl.getX()+25,tl.getY())
    
    charH(win, tl, colour, altColour)
    charI(win, tl2, colour, altColour)


    for y in range(4):
        for x in range (2):
            tl = Point(tlOffset.getX() + x*50, tlOffset.getY() + y*25)
            tl2 = Point(tl.getX()+25,tl.getY())

            charH(win, tl, colour, altColour)
            charI(win, tl2, colour, altColour)
            altColour = not altColour
        
        altColour = not altColour
    
    altColour = True
   
    tl = Point(tlOffset.getX() + 50, tlOffset.getY() + 75)
    tl2 = Point(tl.getX()+25,tl.getY())

    charH(win, tl, colour, altColour)
    charI(win, tl2, colour, altColour)

def blank(win,colour,tlOffset):
    rectangle(win,tlOffset, Point(tlOffset.getX()+100, tlOffset.getY()+100), colour)