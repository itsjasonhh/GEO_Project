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
        return self.name + "(" + str(self.x) + ", " + str(self.y) + ")"
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

#returns two values: slope and y-intercept
def get_equation(p1, p2):
    if p1.x == p2.x and p1.y != p1.y:
        return None, None
    if p1.x == p2.x and p1.y == p2.y:
        return None, None
    else:
        return (p1.y - p2.y)/(p1.x - p2.x), p1.y - p1.x*(p1.y - p2.y)/(p1.x - p2.x)
#Get distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y - p2.y)**2)

def intersect(object1, object2):
    if type(object1) == Segment and type(object2) == Segment:
        if ((object1.point1.y - object1.point2.y)/(object1.point1.x - object1.point2.x) == (object2.point1.y - object2.point2.y)/(object2.point1.x - object2.point2.x)):
            return None
        else:
            m1, b1 = get_equation(object1.point1,object1.point2)
            m2, b2 = get_equation(object2.point1, object2.point2)
            a = Point((b2-b1)/(m1-m2),m1*(b2-b1)/(m1-m2) + b1)
            if not (a.x <= max(object1.point1.x,object1.point2.x) and a.x >= min(object1.point1.x,object1.point2.x)):
                return None
            if not (a.x <= max(object2.point1.x,object2.point2.x) and a.x >= min(object2.point1.x,object2.point2.x)):
                return None
            else:
                return a
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
        if math.sqrt(b1**2 - 4*a*c) < 0:
            return None, None
        if math.sqrt(b1**2 - 4*a*c) == 0:
            x = -b1 / (2*a)
            y = m*x + b
            point = Point(x,y)
            return point, None
        if math.sqrt(b1**2 - 4*a*c) > 0:
            x = (-b1 + math.sqrt(b1**2 - 4*a*c))/(2*a)
            y = m*x + b
            xp = (-b1 - math.sqrt(b1**2 - 4*a*c))/(2*a)
            yp = m*xp + b
            point = Point(x,y)
            point1 = Point(xp,yp)
            return point, point1

    elif type(object1) == Segment and type(object2) == Circle:
        m, b = get_equation(object1.point1,object1.point2)
        x1 = object2.center.x
        y1 = object2.center.y
        y2 = b - y1
        a = m**2 + 1
        b1 = -2*x1 + 2*m*y2
        c = x1**2 + y2**2 - object2.radius ** 2
        if math.sqrt(b1**2 - 4*a*c) < 0:
            return None, None
        if math.sqrt(b1**2 - 4*a*c) == 0:
            x = -b1/(2*a)
            y = m*x + b
            if not(x <= max(object1.point1.x,object1.point2.x) and x >= min(object1.point1.x,object1.point2.x)):
                return None, None
            else:
                return Point(x,y), None
        else:
            x = (-b1 + math.sqrt(b1**2 - 4*a*c))/(2*a)
            y = m*x + b
            xp = (-b1 - math.sqrt(b1**2 - 4*a*c))/(2*a)
            yp = m*xp + b
            if not(x <= max(object1.point1.x,object1.point2.x) and x >= min(object1.point1.x,object1.point2.x)):
                return None, None
            if not(xp <= max(object1.point1.x,object1.point2.x) and x >= min(object1.point1.x,object1.point2.x)):
                return None, None
            else:
                return Point(x,y), Point(xp,yp)

    elif type(object1) == Circle and type(object2) == Segment:
        return intersect(object2, object1)

    else:
        sys.exit("Invalid input!")
geoParser = parsley.makeGrammar("""
    number = ('-' <digit+>:ds -> -int(ds)
                |<digit+>:ds -> int(ds)
                )
    char = <letter>:x -> x
    figure = ("Point" ws? char:p ws? '(' ws? number:x ws? ',' ws? number:y ws? ')' ws? -> Point(p,x,y)
            |"Circle" ws? char:name ws? 'at' ws? '(' ws? number:x ws? ',' number:y ws? ')' ws? 'with' ws? 'radius' ws? number:radius ws? -> Circle(Point(name,x,y),radius)
            |"Segment" ws? 'between' ws? char:a ws? '(' ws? number:x1 ws? ',' ws? number:y1 ws? ')' ws? 'and' ws? char:b ws? '(' ws? number:x2 ws? ',' ws? number:y2 ws? ')' -> Segment(Point(a,x1,y1),Point(b,x2,y2))
            )
    """,{
    "Point": Point,
    "Circle": Circle,
    "Segment": Segment
})
def main():
    turtle.setworldcoordinates(-10,-10,10,10)
    a = geoParser("Segment between A(1,1) and B(2,5)").figure().Draw()
    
main()
#Syntax:
#Point A (2,4)
#Circle C at (2,4) with radiius 10
#Segment between A(1,1) and B(2,5)

