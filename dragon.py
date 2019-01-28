# Ashley Kang / Dragon Curve Fractal

import turtle

def unfold_dragon(n):
    seq = [0]
    #print(seq)

    # TODO
    for i in range(1, n):
        new_seq = seq
        L_reversed = seq[::-1]
        C = []

        for i in range(len(L_reversed)):
            if L_reversed[i] == 0:
                C.append(1)
            else:
                C.append(0)

        new_seq.append(0)

        for i in range(len(C)):
            new_seq.append(C[i])

        #print(new_seq)
        seq = new_seq

    return new_seq

'''
# Test function that generates "unfolding the dragon" sequence
print(unfold_dragon(4))
'''

def dragon(turt, width, n):
    # TODO
    dragon_list = unfold_dragon(n)
    for i in dragon_list:
        if i == 0:
            turt.right(90)
        else:
            turt.left(90)
        turt.forward(10)

turtle.setup(800, 800)
wn = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
#turtle.tracer(0.0)

# Test with first 10 elements in "unfolding the dragon" sequence
dragon(turt, 5, 10)

'''
# Bug? When n is a large number, the turtle freezes
dragon(turt, 5, 10000)
'''

wn.exitonclick()
