import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#000000')
t.speed(50)

for i in range(100):
    for i in range(40):
        t.pu()
        t.goto(10, 100)
        t.pd()
        t.color('#ff0000')
        t.pensize(2)
        t.circle(150, steps=1000)
        t.right(10)
