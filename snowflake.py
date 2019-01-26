# Ashley Kang / Koch Snowflake Fractal

import turtle

def thue_morse(n):
    # TODO
    L = [0]

    for i in range(1, n):
        new_seq = L
        for i in range(len(L)):
            if L[i] == 0:
                new_seq.append(1)
            else:
                new_seq.append(0)
        print(new_seq)
        L = new_seq

    return L
    #return L[:n]

'''
# Test function that generates Thue-Morse sequence
print(thue_morse(6))
'''

def koch(turt, width, n):
    turt.penup()
    turt.goto(0, 300)
    turt.pendown()

    # TODO
    TM_seq = thue_morse(n)
    #print(TMseq)

    for i in TM_seq:
        if TM_seq[i] == 0:
            turt.forward(width)
        else:
            turt.left(60)

turtle.setup(800, 800)
wn = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
#turtle.tracer(0.0)

# Test with first 10 elements in Thue-Morse sequence
koch(turt, 5, 10)

'''
# Bug? When n is a large number, the turtle freezes
koch(turt, 5, 10000)
'''

wn.exitonclick()
