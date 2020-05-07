import turtle


def DrawCurve(turtle, l, order ) :
    if order == 0 :
        turtle.forward(l)
        return
    else :
        l/=3
        DrawCurve(turtle,l,order-1)
        turtle.left(60)
        DrawCurve(turtle,l,order-1)
        turtle.right(120)
        DrawCurve(turtle, l, order-1)
        turtle.left(60)
        DrawCurve(turtle,l,order-1)

if __name__=="__main__":
    turtle.setup(800,600)
    DrawCurve(turtle,300,2)
    turtle.exitonclick()
