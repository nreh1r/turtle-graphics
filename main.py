from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")
screen = Screen()


def draw_square():
    for _ in range(4):
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)


def draw_dashed_line():
    for _ in range(10):
        timmy_the_turtle.forward(15)
        timmy_the_turtle.pencolor("white")
        timmy_the_turtle.forward(15)
        timmy_the_turtle.pencolor("black")


def draw_dashed_line_alternative():
    for _ in range(10):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


def draw_shapes():
    screen.colormode(255)
    counter = 3
    while counter < 11:
        # Generate a new random colour each time
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy_the_turtle.pencolor(r, g, b)
        for _ in range(counter):
            timmy_the_turtle.forward(100)
            turn_angle = 360 / counter
            timmy_the_turtle.right(turn_angle)
        counter += 1


def random_walk(number_of_steps):
    screen.colormode(255)  # -> Can also use turtle.colormode(255)
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed("fastest")
    # Generate a new random colour each time
    counter = 0
    while counter < number_of_steps:
        # Generate a new random color each time
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy_the_turtle.pencolor(r, g, b)
        timmy_the_turtle.forward(50)
        # Choose a random direction to rotate
        rotation = 90 * random.randint(0, 3)
        timmy_the_turtle.setheading(rotation)
        counter += 1


def random_color():
    # Generate a new random color each time
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(gap):
    screen.colormode(255)
    heading = timmy_the_turtle.heading()
    timmy_the_turtle.speed("fastest")
    while heading < 360:
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        heading += gap
        timmy_the_turtle.setheading(heading)


colors_list = [(202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75),
               (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60,
                                                                                                                               72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]


def hirst_painting():
    screen.colormode(255)
    row = 0
    while row < 10:
        timmy_the_turtle.penup()
        timmy_the_turtle.hideturtle()
        timmy_the_turtle.speed("fastest")
        timmy_the_turtle.setx(-250)
        y = -250 + (50 * row)
        timmy_the_turtle.sety(y)
        for _ in range(10):
            timmy_the_turtle.dot(20, random.choice(colors_list))
            timmy_the_turtle.forward(50)
        row += 1


hirst_painting()
screen.exitonclick()
