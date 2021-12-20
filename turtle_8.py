import turtle


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#000000')
t.width(2)
t.speed(15)

col = ('#ffffff', 'pink', 'cyan')
for i in range(300):
    t.pencolor(col[i % 3])
    t.forward(i * 4)
    t.right(121)

