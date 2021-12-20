import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('#7c909c')
t.speed(100)

col = ('#ed7864', '#6e544f', '#592f2f', '#6e382e')
for n in range(5):
    for x in range(8):
        t.speed(x + 10)
        for i in range(2):
            t.pensize(2)
            t.circle(80 + n * 20, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n % 4])
    
