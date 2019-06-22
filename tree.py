from turtle import Turtle

turtle = Turtle()

turtle.color('red', 'yellow')
def tree(length,n):
    if length < (length/n):
           return
    pos = turtle.pos()
    heading = turtle.heading()
    turtle.forward(length)
    turtle.left(30)
    tree(length * 0.5,length/n)
    turtle.left(30)
    tree(length * 0.5,length/n)
    turtle.right(60)
    tree(length * 0.5,length/n)
    turtle.right(30)
    tree(length * 0.5,length/n)
    turtle.right(30)
    tree(length * 0.5,length/n)
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(heading)
    turtle.pendown()
    return

turtle.penup()
turtle.setpos(0, -300)
turtle.left(90)
turtle.pendown()

tree(200,2)



c = input()