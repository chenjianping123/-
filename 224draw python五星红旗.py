
# coding: utf-8

# In[15]:


from turtle import *
setup(600,400,100,100)
up()
goto(-250,150)
down()
pensize(3)
color("black","red")
begin_fill()
goto(-250,-150)
goto(250,-150)
goto(250,150)
goto(-250,150)
end_fill()
color('yellow', 'yellow')
begin_fill()
up()
goto(-180,90)
down()
for i in range(5):
    fd(40)
    right(144)
end_fill()
color('yellow', 'yellow')
begin_fill()
up()
goto(-100,110)
down()
for i in range(5):
    fd(20)
    right(144)
end_fill()
color('yellow', 'yellow')
begin_fill()
up()
goto(-105,80)
down()
for i in range(5):
    fd(20)
    right(144)
end_fill()
color('yellow', 'yellow')
begin_fill()
up()
goto(-120,50)
down()
for i in range(5):
    fd(20)
    right(144)
end_fill()
color('yellow', 'yellow')
begin_fill()
up()
goto(-150,30)
down()
for i in range(5):
    fd(20)
    right(144)
end_fill()

