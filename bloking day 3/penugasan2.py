import turtle
t = turtle.Turtle()
t.speed(3)

def persegi_panjang_warna(p, l, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(2):
        t.forward(p)
        t.right(90)
        t.forward(1)
        t.right(90)
    t.end_fill()

def segitiga_warna(sisi, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for i in range(3):
        t.forward(sisi)
        t.right(120)
    t.end_fill()

#contoh
persegi_panjang_warna(150, 80, "red")
t.penup()
t.goto(-200, 0)
t.pendown()
segitiga_warna(100, "yellow")

turtle.done()