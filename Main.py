import turtle
import sys
import math
import parsley



class Point:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def __str__(self):
        return self.name + "(" + str(round(self.x,4)) + ", " + str(round(self.y,4)) + ")"
    def Draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.dot()
        turtle.write(self.__str__())
        turtle.hideturtle()

class Circle:
    def __init__(self, P, r):
        self.center = P
        self.radius = r
    def __str__(self):
        return "Center: " + str(self.center) + ", radius = " + str(self.radius)
    def Draw(self):
        self.center.Draw()
        turtle.goto(self.center.x + self.radius, self.center.y)
        turtle.setheading(90)
        turtle.pendown()
        turtle.circle(self.radius,360,100)
        turtle.penup()
        turtle.hideturtle()


class Segment:
    def __init__(self, P1, P2):
        self.point1 = P1
        self.point2 = P2
    def __str__(self):
        return "Segment between " + str(self.point1) + " and " + str(self.point2)
    def Draw(self):
        turtle.penup()
        self.point1.Draw()
        turtle.pendown()
        turtle.goto(self.point2.x,self.point2.y)
        self.point2.Draw()
        turtle.write(self.point2)
        turtle.penup()
        turtle.hideturtle()

#Draw line and equation of line or circle
def get_equation(s):
    s.Draw()
    if type(s) == Segment:
        if s.point1.x == s.point2.x and s.point1.y != s.point2.y:
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("Error: vertical line!",False,"left",("Arial",17,"normal"))
            return
        if s.point1.x == s.point2.x and s.point1.y == s.point2.y:
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("Same point!",False,"left",("Arial",17,"normal"))
            return
        else:
            m, b = (s.point1.y - s.point2.y)/(s.point1.x - s.point2.x), s.point1.y - s.point1.x*(s.point1.y - s.point2.y)/(s.point1.x - s.point2.x)
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("y = " + str(m) + "x + " + str(b),False,"left",("Arial",17,"normal"))
            return

    if type(s) == Circle:
        turtle.up()
        turtle.goto(-13,-13)
        turtle.write("(x - " + str(s.center.x) + ")^2 + (y - " + str(s.center.y) + ") ^2 = " + str(s.radius**2),False,"left",("Arial",17,"normal"))
#Draw line segment and length of segment
def length(s):
    s.Draw()
    turtle.up()
    turtle.goto(-13,-13)
    a = math.sqrt((s.point1.x-s.point2.x)**2 + (s.point1.y - s.point2.y)**2)
    turtle.write("Length = " + str(round(a,4)),False,"left",("Arial",17,"normal"))
    return

def intersect(object1, object2):
    object1.Draw()
    object2.Draw()
    if type(object1) == Segment and type(object2) == Segment:
        if ((object1.point1.y - object1.point2.y)/(object1.point1.x - object1.point2.x) == (object2.point1.y - object2.point2.y)/(object2.point1.x - object2.point2.x)):
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
            return
        else:
            m1, b1 = (object1.point1.y - object1.point2.y)/(object1.point1.x - object1.point2.x), object1.point1.y - object1.point1.x*(object1.point1.y - object1.point2.y)/(object1.point1.x - object1.point2.x)
            m2, b2 = (object2.point1.y - object2.point2.y)/(object2.point1.x - object2.point2.x), object2.point1.y - object2.point1.x*(object2.point1.y - object2.point2.y)/(object2.point1.x - object2.point2.x)
            a = Point('P1',(b2-b1)/(m1-m2),m1*(b2-b1)/(m1-m2) + b1)
            if not (a.x <= max(object1.point1.x,object1.point2.x) and a.x >= min(object1.point1.x,object1.point2.x)):
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
                return
            if not (a.x <= max(object2.point1.x,object2.point2.x) and a.x >= min(object2.point1.x,object2.point2.x)):
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
                return
            else:
                a.Draw()
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("Intersection at " + str(a),False,"left",("Arial",17,"normal"))
                return
    elif type(object1) == Circle and type(object2) == Circle:
        x1 = object1.center.x
        x2 = object2.center.x
        y1 = object1.center.y
        y2 = object2.center.y
        r1 = object1.radius
        r2 = object2.radius
        constant = x1**2 + y1**2 - x2**2 - y2**2 -r1**2 + r2**2
        m = (2*x1-2*x2)/(2*y2 - 2*y1)
        b = -constant/(2*y2 - 2*y1)
        a = 1 + m**2
        b1 = -2*x1 + 2*m*b - 2*y1*m
        c = x1**2 + b**2 - 2*y1*b + y1**2 - r1**2
        if b1**2 - 4*a*c < 0:
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
            return
        if b1**2 - 4*a*c == 0:
            x = -b1 / (2*a)
            y = m*x + b
            point = Point('P1',x,y)
            point.Draw()
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("Intersection at " + str(point),False,"left",("Arial",17,"normal"))
            return
        if b1**2 - 4*a*c > 0:
            x = (-b1 + math.sqrt(b1**2 - 4*a*c))/(2*a)
            y = m*x + b
            xp = (-b1 - math.sqrt(b1**2 - 4*a*c))/(2*a)
            yp = m*xp + b
            point = Point('P1',x,y)
            point1 = Point('P2',xp,yp)
            point.Draw()
            point1.Draw()
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("Intersections at " + str(point) + " and " + str(point1),False,"left",("Arial",17,"normal"))
            return
    elif type(object1) == Segment and type(object2) == Circle:
        m, b = (object1.point1.y - object1.point2.y)/(object1.point1.x - object1.point2.x), object1.point1.y - object1.point1.x*(object1.point1.y - object1.point2.y)/(object1.point1.x - object1.point2.x)
        x1 = object2.center.x
        y1 = object2.center.y
        y2 = b - y1
        a = m**2 + 1
        b1 = -2*x1 + 2*m*y2
        c = x1**2 + y2**2 - object2.radius ** 2
        if b1**2 - 4*a*c < 0:
            turtle.up()
            turtle.goto(-13,-13)
            turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
            return
        if b1**2 - 4*a*c == 0:
            x = -b1/(2*a)
            y = m*x + b
            if not(x <= max(object1.point1.x,object1.point2.x) and x >= min(object1.point1.x,object1.point2.x)):
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
                return
            else:
                p1 = Point('P1',x,y)
                p1.Draw()
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("Intersection at " + str(p1) ,False,"left",("Arial",17,"normal"))
                return
        else:
            x = (-b1 + math.sqrt(b1**2 - 4*a*c))/(2*a)
            y = m*x + b
            xp = (-b1 - math.sqrt(b1**2 - 4*a*c))/(2*a)
            yp = m*xp + b
            if not(x <= max(object1.point1.x,object1.point2.x) and x >= min(object1.point1.x,object1.point2.x)):
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
                return
            if not(xp <= max(object1.point1.x,object1.point2.x) and x >= min(object1.point1.x,object1.point2.x)):
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("No intersection points!",False,"left",("Arial",17,"normal"))
                return
            else:
                p1 = Point('P1',x,y)
                p2 = Point('P2',xp,yp)
                p1.Draw()
                p2.Draw()
                turtle.up()
                turtle.goto(-13,-13)
                turtle.write("Intersections at " + str(p1) + " and " + str(p2),False,"left",("Arial",17,"normal"))
                return

    elif type(object1) == Circle and type(object2) == Segment:
        return intersect(object2, object1)

    else:
        sys.exit("Invalid input!")
geoParser = parsley.makeGrammar("""
    number = ('-' <digit+>:ds -> -int(ds)
                |<digit+>:ds -> int(ds)
                )
    char = <letter>:x -> x
    point = "Point" ws? char:p ws? '(' ws? number:x ws? ',' ws? number:y ws? ')' ws? -> Point(p,x,y)
    circle = "Circle" ws? 'at' point:p1 ws? 'with' ws? 'radius' ws? number:radius ws? -> Circle(p1,radius)
    segment = "Segment" ws? 'between' ws? point:p1 ws? 'and' ws? point:p2 -> Segment(p1, p2)
    figure = (point
            | circle
            | segment
            )
    commands = ("Length" ws? "of" ws? segment:s ws? -> length(s)
                |"Equation" ws? "of" ws? figure:a ws? -> get_equation(a)
                |"Intersection" ws? "of" ws? figure:f1 ws? "and" ws? figure:f2 ws? -> intersect(f1,f2)
                
    
    )
    """,{
    "Point": Point,
    "Circle": Circle,
    "Segment": Segment,
    "length": length,
    "get_equation": get_equation,
    "intersect": intersect

})
def drawCoordinatePlane():
    #Draws axes
    turtle.setworldcoordinates(-15,-15,15,15)
    turtle.speed(0)
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(0,-10)
    turtle.pendown()
    turtle.forward(20)
    turtle.setheading(180)
    turtle.penup()
    turtle.goto(10,0)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    #Draws labels
    for i in range(-10,11,1):
        turtle.penup()
        turtle.goto(i,-0.5)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(1)
    for i in range(-10,11,1):
        turtle.penup()
        turtle.goto(-0.5, i)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(1)
    turtle.hideturtle()


def main():
    drawCoordinatePlane()
    #a = geoParser("Intersection of Circle at Point A(2,3) with radius 3  and Circle at Point B(1,-1) with radius 4").commands()
    #b = geoParser("Intersection of Segment between Point A(-10,5) and Point B(10,5) and Circle at Point C(0,0) with radius 5").commands()
    a = geoParser("Equation of Circle at Point A(2,3) with radius 3").commands()
    turtle.exitonclick()
main()

#test cases for length, equation, intersection

