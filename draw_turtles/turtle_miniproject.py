import turtle


def draw_initials():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow")
    brad.speed(1)

    brad.left(90)
    brad.forward(200)
    brad.backward(100)
    brad.right(45)
    brad.forward(138)
    brad.backward(138)
    brad.right(90)
    brad.forward(138)

    brad.left(45)
    brad.penup()
    brad.forward(100)
    brad.pendown()
    brad.forward(100)
    brad.backward(100)
    brad.left(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(100)

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)

    # tri = turtle.Turtle()
    # tri.shape("triangle")
    # tri.color("green")
    # tri.speed(2)
    #
    # for i in range(3):
    #     tri.forward(100)
    #     tri.left(120)

    window.exitonclick()


draw_initials()
