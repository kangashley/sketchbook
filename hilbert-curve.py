# Ashley Kang / Hilbert Curve L-System

'''
Axiom: L
Rule 1: L -> +RF-LFL-FR+
Rule 2: R -> -LF+RFR+FL-
Turn 90 degrees

Graphics encoding in Turtle:
F = move forward
B = move backward
+ = turn right
- = turn left
'''

import turtle

# Define axiom rules
def applyRules(ch):
    newStr = ""
    if ch == 'L': # Axiom
        newStr = '+RF-LFL-FR+' # Rule 1
    elif ch == 'R':
        newStr = '-LF+RFR+FL-' # Rule 2
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
print(createLsystem(2, "L"))
# Output: +-LF+RFR+FL-F-+RF-LFL-FR+F+RF-LFL-FR+-F-LF+RFR+FL-+
'''

# Draw L-system based on turtle object, instructions, angle, and distance
def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLsystem(6, "L")
    print(inst)

    turt = turtle.Turtle()
    wn = turtle.Screen()

    turt.speed(0)
    #turtle.tracer(0.0)
    turt.penup()
    turt.setposition(-150, 0)
    turt.pendown()
    drawLsystem(turt, inst, 90, 5)

    wn.exitonclick()

main()
