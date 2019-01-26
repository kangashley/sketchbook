# Ashley Kang / Twig L-System

'''
Axiom: X
Rule 1: X -> F+[[X]-X]-F[-FX]+X
Rule 2: F -> FF
Turn 25 degrees

Graphics encoding in Turtle:
F = move forward
B = move backward
+ = turn right
- = turn left
[ = save current state
] = restore most recent state
'''

import turtle

# Define axiom rules
def applyRules(ch):
    newStr = ""
    if ch == 'X': # Axiom
        newStr = 'F+[[X]-X]-F[-FX]+X' # Rule 1
    elif ch == 'F':
        newStr = 'FF' # Rule 2
    else:
        newStr = ch # Keep character in string
    return newStr

# Produce a new string based on axiom rules
def processString(oldStr):
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRules(ch)
    return newStr

# Create L-system based on number of iterations and axiom
def createLsystem(numIterations, axiom):
    startStr = axiom
    endStr = ""
    for i in range(numIterations):
        endStr = processString(startStr)
        startStr = endStr
    return endStr

'''
# Test L-system with 2 iterations
print(createLsystem(2, "X"))
# Output: FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X
'''

# Draw L-system based on turtle object, instructions, angle, and distance
def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfoList = []

    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

def main():
    inst = createLsystem(6, "X")
    print(inst)

    turt = turtle.Turtle()
    wn = turtle.Screen()

    turt.speed(0)
    #turtle.tracer(0.0)
    turt.penup()
    turt.setposition(-200, 0)
    turt.pendown()
    drawLsystem(turt, inst, 25, 5)

    wn.exitonclick()

main()
