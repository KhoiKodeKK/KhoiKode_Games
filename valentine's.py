import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

turtle.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-130,130)
t.pendown()
t.color('white')
t.write("Happy Valentine's day",font=("Verdana",16,'bold'))

t.penup()
t.goto(-150,-180)
t.pendown()
t.color('white')
t.write("Have a good day!",font=("Verdana",25,'bold'))


turtle.done()