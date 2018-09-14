
# coding: utf-8

# In[ ]:


#动态Python.py
import turtle
turtle.setup(800,400,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.pencolor("purple")
    turtle.circle(-40,80)
    turtle.pencolor("gold")
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.pencolor("darkgreen")
turtle.fd(40*2/3)
turtle.circle(-16,90)
turtle.pencolor("violet")
turtle.fd(40)
turtle.circle(40,180)
turtle.pencolor("gold")
turtle.circle(-40,180)
turtle.circle(-40,360)

