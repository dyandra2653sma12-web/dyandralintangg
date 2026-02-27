import turtle
import math

#Konfigurasi Layar
screen = turtle.Screen()
screen.setup(700,700)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

#Kecepatan maksimal
def draw_filled_circle(radius,color, x=0, y=0):
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_text_curved(text,radius,start_angle,step,font_size):
    t.penup()
    angle = start_angle
    for char in text:
        x = radius *
        math.cos(math.radians(angle))
            y = radius *
        math.sin(math.radians(angle))
            t.goto(x,y)
            t.setheadinga(angle-90 if start_angle>0 else angle + 90)
            t.forward(10 if start_angle>0 else - 20)
#penyesuaian posisi huruf
t.pencolor("black")
t.write(char,align="center", font=("Arial", font_size, "bold"))
angle += step

def draw_star(x,y,size):
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.color("black")
    t.begin_fill()
    for_in range(5)
      t.forward(size)
      t.right(144)
    t.end_fill()

#1.Lingkaran Putih Luar (Border)
draw_filled_circle(260, "black")
draw_filled_circle(255,"white")

#2.Lingkaran Biru Tengah
draw_filled_circle(200,"#1a316c")