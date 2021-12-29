# from turtle import *
# t1 = Turtle()
# colors = ["red","orange","yellow","green","indigo","violet"]
# import random
# t1.goto (-200,0)
# t1.down()
# t1.width(5)
# t1.hideturtle()
# t1.speed(0)
# for i in range (100):
#     colorchoice = random.choice(colors)
#     t1.color (colorchoice)
#     t1. forward (300)
#     t1.right(87)

# import random
# from turtle import *
# t = Turtle()
# color = ["red","blue","pink","green","orange"]
# import random
# t.hideturtle()
# t.up()
# t.goto(-200,0)
# t.down()
# t.width(1)
# bgcolor("black")
# t.speed(0)
# for i in range (400):
#     colorchoice = random.choice(color)
#     t.color(colorchoice)
#     t.forward(400)
#     t.right(181)


# import turtle
# def fleur():
#     for i in range(300):
#         turtle.speed(0)
#         turtle.hideturtle()
#         turtle.circle(190-i,90)
#         turtle.left(90)
#         turtle.circle(190-i,90)
#         turtle.left(38)
# fleur()
# turtle.mainloop()



import turtle
t = turtle.Turtle()
t.goto(-250,0)
t.hideturtle()
color =["red","blue","yellow","black","green"]
t.width(5)
import random
for i in range(200):
    colorchoice = random.choice(color)
    t.color(colorchoice)
    t.forward(50)
    # t.circle(190-1,90)
    t.right(20)
    # t.circle(-190-1,90)
    t.left(40)
# t.hideturtle()
# t.fleur()
# t.mainloop



