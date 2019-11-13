import turtle
bob = turtle.Turtle()



def smol():
    bob.begin_fill()
    for times in range(4):
        bob.forward(10)
        bob.left(90)
    bob.end_fill()
