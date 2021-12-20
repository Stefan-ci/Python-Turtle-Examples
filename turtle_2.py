import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

col = ('yellow', 'red', 'pink', 'cyan', 'aqua', 'green', 'blue')
for i in range(150):
    t.pencolor(col[i%6])
    t.pencolor(col[i % 6])
    t.circle(198-1/2, 99)
    t.lt(90)
    t.circle(199-1/3, 98)
    t.lt(60)
