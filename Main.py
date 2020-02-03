import turtle
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def Draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.dot()
        turtle.hideturtle()

class Circle:
    def __init__(self, P, r):
        self.center = P
        self.radius = r
    def __str__(self):
        return "Center: " + str(self.center) + ", radius = " + str(self.radius)
    def Draw(self):
        turtle.penup()
        turtle.goto(self.center.x + self.radius, self.center.y)
        turtle.pendown()
        turtle.circle(self.radius)
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
        turtle.goto(self.point1.x,self.point1.y)
        turtle.dot()
        turtle.pendown()
        turtle.goto(self.point2.x,self.point2.y)
        turtle.dot()
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

def intersect(s1, s2):
    if ((s1.point1.y - s1.point2.y)/(s1.point1.x - s1.point2.x) == (s2.point1.y - s2.point2.y)/(s2.point1.x - s2.point2.x)):
        return None
    else:
        m1, b1 = get_equation(s1.point1,s1.point2)
        m2, b2 = get_equation(s2.point1, s2.point2)
        a = Point((b2-b1)/(m1-m2),m1*(b2-b1)/(m1-m2) + b1)
        if not (a.x <= max(s1.point1.x,s1.point2.x) and a.x >= min(s1.point1.x,s1.point2.x)):
            return None
        if not (a.y <= max(s1.point1.y,s1.point2.y) and a.y >= min(s1.point1.y,s1.point2.y)):
            return None
        if not (a.x <= max(s2.point1.x,s2.point2.x) and a.x >= min(s2.point1.x,s2.point2.x)):
            return None
        if not (a.y <= max(s2.point1.y,s2.point2.y) and a.y >= min(s2.point1.y,s2.point2.y)):
            return None
        else:
            return a





def main():
    s1 = Segment(Point(0,2),Point(2,4))
    s2 = Segment(Point(5,-21),Point(2,-3))
    print(intersect(s1,s2))



main()