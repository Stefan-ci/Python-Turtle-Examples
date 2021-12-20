import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('white')
t.pencolor('pink')
t.speed(0)

for i in range(250):
    t.circle(190-1, 90)
    t.lt(98)
    t.circle(100)
    t.lt(18)
# s.exitonclick()
