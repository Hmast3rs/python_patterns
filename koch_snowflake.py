import turtle
from math import pi, sin, cos

def genThueMorse(bits):
    value = 0
    for n in range(bits):     
        x = n ^ (n-1)                         
        if ((x ^ (x>>1)) & 0x55555555):
            value = 1 - value
        yield value

def tp(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def KochSnowflake(centrex, centrey, n, size, rotation = 0):
    tp(centrex + size*3**(-3/2) * cos(rotation/180*pi + pi/6),
       centrey - size*3**(-3/2) * sin(rotation/180*pi + pi/6))
    turtle.setheading(-rotation)
    
    edge = size/3**n
    for i in range(3):
        for j in genThueMorse(2**(2*n-1)):
            if j:
                turtle.forward(edge)
                turtle.left(60)
            else:
                turtle.left(180)

turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor(0,0,0)
turtle.pencolor(0.1,0.1,0.1)
turtle.setup(turtle.window_width()*2, turtle.window_height()*4/3)

#x = turtle.window_height() * 2
x = 60

def z():
    for n in range(1,7):
        c = 0.1 * n
        turtle.pencolor(c,c,c)
        KochSnowflake(0, 0, n, x, 0)
def y():
    for i in range(0,5):
        c = 0.1 * (i+1)
        turtle.pencolor(c,c,c)
        KochSnowflake(0, 0, i+2, 180 * 3**(i/2), 90*i)

def w():
    for i in range(2,5):
        c = 0.1 * (i-1)
        turtle.pencolor(c,c,c)
        for j in range(0,6):
            KochSnowflake(
                x*3**(-(7-2*i)/2)*2 * cos(pi/6 - pi/3 * j),
                x*3**(-(7-2*i)/2)*2 * sin(pi/6 - pi/3 * j),
                i, x*3**(i-2))
    
turtle.onkey(w, "Up")
turtle.listen()
