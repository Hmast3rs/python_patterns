
import turtle
from random import randint
from math import sin, cos, pi

def tp(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def regularPolygon(x, n, theta=0, flip=False):
    return [[x*cos(i*2*pi/n+theta),x*sin(i*2*pi/n+theta)] for i in (range(n-1,-1,-1) if flip else range(n))]

turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor(0,0,0)
turtle.pencolor(0.2,0.2,0.2)
turtle.setup(turtle.window_width()*2, turtle.window_height()*4/3)
turtle.tracer(0, 0)

m = 400
originPoint = (randint(-m,m), randint(-m,m))

# r = 708/1000
# octogon = regularPolygon(m, 8, pi/8)
# for i in range(50000):

#    targetPoint = octogon[randint(0,len(octogon)-1)]

#    v = [targetPoint[0]-originPoint[0], targetPoint[1]-originPoint[1]]
#    v = [v[0]*r, v[1]*r]
   
#    originPoint = [originPoint[0]+v[0], originPoint[1]+v[1]]
#    teleport(originPoint[0], originPoint[1])
#    turtle.dot(2, "blue")

# r = 692/1000
# heptagon = regularPolygon(m, 7, pi/14)
# for i in range(50000):

#    targetPoint = heptagon[randint(0,len(heptagon)-1)]

#    v = [targetPoint[0]-originPoint[0], targetPoint[1]-originPoint[1]]
#    v = [v[0]*r, v[1]*r]
   
#    originPoint = [originPoint[0]+v[0], originPoint[1]+v[1]]
#    teleport(originPoint[0], originPoint[1])
#    turtle.dot(2, "blue")

# r = 2/3
# hexagon = regularPolygon(m, 6, 0)
# for i in range(50000):

#    targetPoint = hexagon[randint(0,len(hexagon)-1)]

#    v = [targetPoint[0]-originPoint[0], targetPoint[1]-originPoint[1]]
#    v = [v[0]*r, v[1]*r]
   
#    originPoint = [originPoint[0]+v[0], originPoint[1]+v[1]]
#    teleport(originPoint[0], originPoint[1])
#    turtle.dot(2, "blue")

# r = 0.62
# pentagon = regularPolygon(m, 5, pi/10)
# for i in range(50000):

#    targetPoint = pentagon[randint(0,len(pentagon)-1)]

#    v = [targetPoint[0]-originPoint[0], targetPoint[1]-originPoint[1]]
#    v = [v[0]*r, v[1]*r]
   
#    originPoint = [originPoint[0]+v[0], originPoint[1]+v[1]]
#    teleport(originPoint[0], originPoint[1])
#    turtle.dot(2, "blue")

# r = 2/3
# square = regularPolygon(m, 4, -pi/4)
# for i in range(50000):

#    targetPoint = square[randint(0,len(square)-1)]

#    v = [targetPoint[0]-originPoint[0], targetPoint[1]-originPoint[1]]
#    v = [v[0]*r, v[1]*r]
   
#    originPoint = [originPoint[0]+v[0], originPoint[1]+v[1]]
#    teleport(originPoint[0], originPoint[1])
#    turtle.dot(2, "blue")

r = 1/2
triangle = regularPolygon(m, 3, -pi/6)
triangle = [[p[0],p[1]-m*(1-cos(pi/6))] for p in triangle]

for i in range(10000):
    targetPoint = triangle[randint(0,len(triangle)-1)]

    v = [targetPoint[0]-originPoint[0], targetPoint[1]-originPoint[1]]
    v = [v[0]*r, v[1]*r]
    
    originPoint = [originPoint[0]+v[0], originPoint[1]+v[1]]
    tp(originPoint[0], originPoint[1])
    turtle.dot(2, "blue")
