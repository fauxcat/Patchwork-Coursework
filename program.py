from graphics import *

#Here we draw the simple objects to be combined into the patches

def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint

def rectangle(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.draw(win)
    return r

def charH(win,tlPoint, colour, alt):
    bg = Rectangle(tlPoint, Point(tlPoint.getX()+25, tlPoint.getY()+25))
    hPart1 = Rectangle(Point(tlPoint.getX()+5, tlPoint.getY()), Point(tlPoint.getX()+20,tlPoint.getY()+10))
    hPart2 = Rectangle(Point(tlPoint.getX()+5, tlPoint.getY()+15), Point(tlPoint.getX()+20, tlPoint.getY()+25))
    
    if alt == True:
        bg.setFill(colour)
        hPart1.setFill("white")
        hPart2.setFill("white")
        hPart1.setOutline("white")
        hPart2.setOutline("white")
    else:
        hPart1.setFill(colour)
        hPart2.setFill(colour)
        hPart1.setOutline(colour)
        hPart2.setOutline(colour)
        bg.setFill("white")


    bg.draw(win)
    hPart1.draw(win)
    hPart2.draw(win)


    return bg, hPart1, hPart2

def charI(win,tlPoint, colour, alt):
    bg = Rectangle(tlPoint, Point(tlPoint.getX()+25, tlPoint.getY()+25))
    iPart1 = Rectangle(Point(tlPoint.getX(),tlPoint.getY()+5), Point(tlPoint.getX()+10,tlPoint.getY()+20))
    iPart2 = Rectangle(Point(tlPoint.getX()+15, tlPoint.getY()+5), Point(tlPoint.getX()+25, tlPoint.getY()+20))

   
    if alt == True:
        bg.setFill(colour)
        iPart1.setFill("white")
        iPart2.setFill("white")
        iPart1.setOutline("white")
        iPart2.setOutline("white")
    else:
        iPart1.setFill(colour)
        iPart2.setFill(colour)
        iPart1.setOutline(colour)
        iPart2.setOutline(colour)
        bg.setFill("white")

    bg.draw(win)
    iPart1.draw(win)
    iPart2.draw(win)

    return bg, iPart1, iPart2

###################################################################################################

#Here we create the patches with the graphical object functions
#patch1 is the penultimate patch
#patch2 is the final patch
#blank is used for blank patches

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

def patch2(win, colour, tlOffset):
    for y in range(0,100,10):
        x = 90-y
        x = tlOffset.getX() + x
        y = tlOffset.getY() + y
        rectangle(win, Point(x,y), Point(x+10,y+10), colour)

def blank(win,colour,tlOffset):
    rectangle(win,tlOffset, Point(tlOffset.getX()+100, tlOffset.getY()+100), colour)

###################################################################################################

#Here we draw the graphic window, ask for the user input and draw the patches based on the inputs.

def main():
    size = int(input("What size patchwork would you like? (5/7)"))
    while size != 5 and size != 7:
        print("Invalid patchwork size")
        size = int(input("What size patchwork would you like? (5/7)"))
    
    screenSize = size*100
    colours = ["red", "green", "blue", "purple", "orange", "cyan"]
    chosenColours = []

    for i in range(3):
        userColour = str(input("Choose a colour from the list (red, green, blue, purple, orange, cyan) : "))
        while userColour not in colours:
            userColour = str(input("Invalid Colour! Choose a colour from the list (red, green, blue, purple, orange, cyan) : "))
        chosenColours.append(userColour)
    
    win = GraphWin("Test", screenSize, screenSize)
    tlPoint = Point(0,0)

    if size == 5:
        for y in range(0, screenSize, 100):
            for x in range(0, screenSize, 100):
                tlPoint = Point(x,y)
                if (tlPoint.getX() >= 100 and tlPoint.getX() < 400 and tlPoint.getY() >= 100 and tlPoint.getY() < 400):
                    usedColour = chosenColours[2]
                    if (tlPoint.getX() == tlPoint.getY() and tlPoint.getX() < 400):
                        patch2(win,usedColour,tlPoint)
                    elif(tlPoint.getY() == 200 and tlPoint.getX() < 400):
                        patch1(win,usedColour,tlPoint)
                    elif(tlPoint.getX()<400 and tlPoint.getY()<400):
                        blank(win,usedColour,tlPoint)
                
                elif (tlPoint.getX() == tlPoint.getY()):
                    usedColour = chosenColours[0]
                    patch2(win,usedColour,tlPoint)
                
                elif((tlPoint.getX() % 200 == 0) and (tlPoint.getY() % 200 == 0)):
                    usedColour = chosenColours[0]
                    patch1(win,usedColour,tlPoint)
                
                else:
                    usedColour = chosenColours[1]
                    if(tlPoint.getY()<100 or tlPoint.getY()>=400):
                        patch1(win,usedColour,tlPoint)
                    else:
                        blank(win,usedColour,tlPoint)
                
    if size == 7:
        for y in range(0, screenSize, 100):
            for x in range(0, screenSize, 100):
                tlPoint = Point(x,y)
                if (tlPoint.getX() >= 100 and tlPoint.getX() <=500  and tlPoint.getY() >=100 and tlPoint.getY() <= 500):
                    usedColour = chosenColours[2]
                    if ((tlPoint.getY() == 200 or tlPoint.getY() == 400) and tlPoint.getX() != tlPoint.getY()):
                        patch1(win,usedColour,tlPoint)
                    elif (tlPoint.getY() == tlPoint.getX()):
                        patch2(win,usedColour,tlPoint)
                    else:
                        blank(win,usedColour,tlPoint)
                
                elif (tlPoint.getX() == tlPoint.getY()):
                    usedColour = chosenColours[0]
                    patch2(win,usedColour,tlPoint)
                
                elif((tlPoint.getX() % 200 == 0) and (tlPoint.getY() % 200 == 0)):
                    usedColour = chosenColours[0]
                    patch1(win,usedColour,tlPoint)
                
                else:
                    usedColour = chosenColours[1]
                    if(tlPoint.getY()<100 or tlPoint.getY()>=600):
                        patch1(win,usedColour,tlPoint)
                    else:
                        blank(win,usedColour,tlPoint)
    win.getMouse()

main()