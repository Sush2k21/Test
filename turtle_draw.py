import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(11)
clr_list=['red','green','yellow','blue','white','Orange','purple']
for i in range(6):
    for colors in clr_list:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(50)
    
turtle.done()