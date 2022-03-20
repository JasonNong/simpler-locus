import turtle

class Locus:
    def __init__(self):
        self.my_turtle = turtle.Pen()

    
    def set_turtle(self):
        self.my_turtle.shape('circle')
        self.my_turtle.shapesize(0.3, 0.3, 1)


    def to_center(self, len):
        self.my_turtle.penup()
        self.my_turtle.left(90)
        self.my_turtle.forward(len)
        self.my_turtle.pendown()


    def make_circle(self, len):
        self.my_turtle.penup()
        self.my_turtle.forward(len)
        self.my_turtle.pendown()
        self.my_turtle.circle(len)

    
    def around_point(self):
        self.radius = float(input("Enter the radius [cm]")) * 10
        self.my_turtle.fillcolor('blue')
        self.set_turtle()
        self.my_turtle.begin_fill()
        self.my_turtle.circle(self.radius)
        self.my_turtle.end_fill()
        self.to_center(self.radius)

        print("The area in blue is every point within the radius of ", self.radius/10, "cm")
        turtle.done()


    def two_points(self):
        a = float(input("What is the radius of point A? [cm]")) * 10
        b = float(input("What is the radius of point B? [cm]")) * 10
        len = float(input("About how far are the points from each other? [cm]")) * 10

        self.set_turtle()
        self.make_circle(a)
        self.to_center(a)
        
        self.my_turtle.penup()
        self.my_turtle.right(90)
        self.my_turtle.forward(len + b)
        self.my_turtle.pendown()

        self.my_turtle.left(90)
        self.my_turtle.circle(b)
        self.to_center(b)
            
        print("\nThe overlapping area is all the locus of points")        
        turtle.done()
    

def main():
    run = Locus()
    point = int(input("Do you have 1 or 2 points? "))
    if point == 1:
        run.around_point()
    else:
        run.two_points()


if __name__ == '__main__':
    main()
    