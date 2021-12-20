import turtle

t = turtle.Pen()

turtle.bgcolor('black')
t.pencolor('red')
t.speed(0)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for i in range(360):
    t.pencolor(colors[i%6])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)
# s.exitonclick()
