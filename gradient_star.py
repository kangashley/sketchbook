# Ashley Kang / Turtle Gradient Star

import turtle

turtle.setup(800, 800)
wn = turtle.Screen()
wn.colormode(1.0)

ike = turtle.Turtle()

UNIT = 200

START_COLOR = 0.0 # Blue: (0, 0, 1)
END_COLOR = 1.0 # Purple: (1, 0, 1)
COUNT = 72

INCREASE = float(END_COLOR / COUNT)

def drawStar(turtle, UNIT):
    # Initialize gradient color
    gradient = 0

    # Loop for drawing strokes
    # Starts at 0 degrees and increments counterclockwise by 5 degrees
    # until it reaches 360 degrees
    for i in range(0, 360, 5):
        # Increase gradient color by 1 / 72
        gradient += INCREASE
        # Make color and set it to pencolor
        color = (gradient, 0, 1)
        ike.pencolor(color)
        # Draw stroke
        ike.setheading(i)
        ike.forward(UNIT)
        ike.backward(UNIT)

# Call function to draw Gradient Star
drawStar(ike, UNIT)

wn.exitonclick()
