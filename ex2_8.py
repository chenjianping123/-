import turtle
edge = 15
turtle.setup(500,500,0,0)
turtle.penup()
for i in range(8):
    turtle.fd(edge)
    turtle.pendown()    
    turtle.left(90)
    
    turtle.fd(edge)
    turtle.left(90)
    
    edge = edge + 10
    turtle.fd(edge)    
    turtle.left(90)
    
    turtle.fd(edge)
    turtle.left(90)
    
    edge = edge + 10
import turtle as t
edge = 5
step = 5
def draw():
    global edge
    t.fd(edge)
    if t.isdown() == False:
        t.pendown()
    t.left(90)
    t.fd(edge)
    t.left(90)
    edge += step
    t.fd(edge)
    t.left(90)
    t.fd(edge)
    t.left(90)
    edge += step
    t.setup(600,400,20,20)
    t.penup()
for i in range(8):
    draw()
