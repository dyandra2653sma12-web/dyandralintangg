import turtle

t = turtle.Turtle()
t.speed(3)

#persegi panjang
t.penup()
t.goto(-200,100)
t.pendown()
for i in range(2):
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.right(90)

#Segitiga
t.penup()
t.goto(0,100)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)

#Trapesium
t.penup()
t.goto(200,100)
t.pendown()
t.forward(120)
t.left(120)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)

#Jajar Genjang
t.penup()
t.goto(-200,-100)
t.pendown()
t.forward(120)
t.left(60)
t.forward(60)
t.left(120)
t.forward(120)
t.left(60)
t.forward(60)

#Belah Ketupat
t.penup()
t.goto(100,-100)
t.pendown()
for i in range(4):
    t.forward(80)
    t.left(60 if i % 2 == 0 else 120)

turtle.done()