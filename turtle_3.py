import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('white')
t.pencolor('red')
t.speed(50)

for i in range(250):
    t.circle(100)
    t.lt(1)
    t.circle(100)
    t.lt(1)
# s.exitonclick()
