from graphics import *

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


    