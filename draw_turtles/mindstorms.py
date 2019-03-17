import turtle


def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("yellow")
    brad.speed(2)

    for i in range(36):
        draw_square(brad)
        brad.right(10)

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


draw_art()
