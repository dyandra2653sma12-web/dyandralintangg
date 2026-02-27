import turtle

t = turtle.Turtle
t.speed(0)

def fib_tree(n, panjang):
    if n == 0:
        return
    t.forward(panjang)
    t.left(30)
    fib_tree(n-1, panjang*0.7)
    t.right(60)
    fib_tree(n-1, panjang*0.7)
    t.left(30)
    t.backward(panjang)

fib_tree(8, 100)
turtle.done()