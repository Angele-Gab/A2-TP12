import turtle
def drawCurve(turtle, l,n) :
    if n == 0 :
        turtle.exitonclick()
    turtle.down()
    turtle.forward(l/3)
    turtle.left(60)
    turtle.forward(l/3)
    turtle.right(120)
    turtle.forward(l/3)
    turtle.left(60)
    turtle.forward(l/3)
    turtle.left(60)


    drawCurve(turtle,l,n-1)

turtle.setup(500, 500)
turtle.shape("turtle")
drawCurve(turtle, 150,6)
turtle.exitonclick()



