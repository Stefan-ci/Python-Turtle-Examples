import turtle

a = 0
b = 0

turtle.bgcolor('#000000')
turtle.speed(0)
turtle.pencolor('#00ff00')
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a += 1
    b += 0.25
