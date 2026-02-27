import turtle
t = turtle.Turtle()
t.speed(3)

#Merah
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

#putih
t.right(90)
t.forward(100)
t.left(90)
t.fillcolor("white")
t.begin_fill()
for i in range (2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

turtle.done()