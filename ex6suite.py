from Ex6 import *

def DrawSnowFlake(turtle, l, order):
    for i in range(0,3) :
        DrawCurve(turtle,l,order)
        turtle.right(120)


if __name__=="__main__":
    turtle.setup(800,600)
    DrawSnowFlake(turtle,300,3)
    turtle.exitonclick()
