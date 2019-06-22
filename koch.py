from turtle import Turtle

t = Turtle()

t.color('red', 'yellow')
def Recursive_Koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        Recursive_Koch(length, depth-1)
        t.right(60)
        Recursive_Koch(length, depth-1)
        t.left(120)
        Recursive_Koch(length, depth-1)
        t.right(60)
        Recursive_Koch(length, depth-1)
# ----------

t.penup()
t.penup()
t.setpos(-150,-150)
t.pendown()
print(t.pos())
LENGTH=10
LEVEL=3
for i in range(6):
    Recursive_Koch(LENGTH, LEVEL)
    t.left(60)


c = input()