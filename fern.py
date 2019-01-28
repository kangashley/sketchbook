# Ashley Kang / Barnsley Fern Fractal
import random, turtle

def barnsley_fern(turt, count):
    x = y = 0

    # TODO
    for i in range(count):
        # Generate a pseudorandom number to select 1 of 4 transforms (nx, ny)
        nx = random.randrange(-800, 800)
        ny = random.randrange(-800, 800)

        percent = random.randrange(0, 100)
        # 1% of the time, move down stem
        if (percent <= 1):
            nx = 0
            ny = 0.16 * y
        # 85% of the time, move from large to small leaf
        elif (percent > 1 and percent <= 86):
            nx = (0.85 * x) + (0.04 * y)
            ny = (-0.04 * x) + (0.85 * y) + 1.6
        # 7% of the time, move from small to large leaf
        elif (percent > 86 and percent <= 93):
            nx = (0.2 * x) - (0.26 * y)
            ny = (0.23 * x) + (0.22 * y) + 1.6
        # 7% of the time, flip sides
        elif (percent > 93 and percent <= 100):
            nx = (-0.15 * x) + (0.28 * y)
            ny = (0.26 * x) + (0.24 * y) + 0.44

        # Draw a green dot at (x, y), scaled to window size
        x = nx
        y = ny
        turt.penup()
        turt.goto(x * 50, y * 50 - 300)
        turt.pendown()
        turt.dot(3, "green")

turtle.setup(800, 800)
wn = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
#turtle.tracer(0.0)
barnsley_fern(turt, 10000)

wn.exitonclick()
