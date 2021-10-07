# import turtle
# pen=turtle.Turtle()
# def curve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)
# def heart():
#     pen.fillcolor('red')                                                                                                                                                                                                          
#     pen.begin_fill() 
#     pen.left(140)  
#     pen.forward(113)  
#     curve ()
#     pen .left(120)
#     curve ()
#     pen.forward(112)
#     pen.end_fill()
# def txt():
#     pen.up()
#     pen.setpos(-68,95)
#     pen.down()
#     pen.color('black')
#     pen.write("Shraddha",font=("z003",30,"bold"))
# heart()
# txt()
# pen.ht()


# import turtle
# loadwindow=turtle.Screen()
# turtle.speed(6)
# for i in range(100):
#     turtle.circle(5*i)
#     turtle.circle(-5*i)
#     turtle.left(i)

# turtle.exitonclick()  


# import turtle
# colors=['red','purple','blue','green','orange','yellow']
# t=turtle.Pen() 
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)


import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(10):
    for colours in ["red","violet","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)    