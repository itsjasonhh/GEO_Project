import turtle

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

def main():
    p = Point(3, 10)
    p1 = Point(100,100)
    c = Segment(p,p1)
    c.Draw()



main()