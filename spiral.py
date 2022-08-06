
import turtle
from math import sin, cos, sqrt, pi

def tp(p):
    turtle.penup()
    turtle.goto(p[0], p[1])
    turtle.pendown()

def line(p1, p2):
    tp(p1)
    turtle.goto(p2)

def polygon(vertices):
    n = len(vertices)
    for i in range(n):
        line(vertices[i], vertices[(i+1)%n])

def spiral(vertices):
    d = 10
    n = len(vertices)
    while d > 1:
        polygon(vertices)

        newVertices = []
        for i in range(n):
            p1, p2 = vertices[i], vertices[(i+1)%n]

            v = (p2[0]-p1[0], p2[1]-p1[1])
            m = sqrt(v[0]**2 + v[1]**2)
            if m < d+1:
                d -= 1
            v = (v[0]*d/m, v[1]*d/m)

            newVertices.append((p1[0]+v[0], p1[1]+v[1]))
        vertices = newVertices

def regularPolygon(x, n, theta=0, flip=False):
    return [[x*cos(i*2*pi/n+theta),x*sin(i*2*pi/n+theta)] for i in (range(n-1,-1,-1) if flip else range(n))]
        
turtle.speed(0)
# turtle.speed(1)
turtle.hideturtle()
turtle.bgcolor(0,0,0)
turtle.pencolor(0.3,0.3,0.3)

x = 40
n = 4

square = regularPolygon(x, 4, pi/4)
square2 = regularPolygon(x, 4, pi/4, True)

spiral(regularPolygon(8*x, 8))

toggle = False
for i in range(-12,13):
    for j in range(-6,7):
        spiral([[p[0]+i*x*2*cos(pi/4),p[1]+j*x*2*sin(pi/4)] for p in (square if toggle else square2)])
        toggle = not toggle
