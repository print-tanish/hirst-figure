# import colorgram 
# colors=colorgram.extract('hirst.jpg',8)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as t
t.colormode(255)
color_list=[(239, 239, 236), (235, 229, 232), (230, 236, 231), (234, 35, 109), (237, 73, 34), (152, 27, 63), (6, 148, 95), (212, 228, 234)]
def random_color():
    random_color_need = random.choice(color_list)
    return random_color_need

import random

tim = t.Turtle()
count_dot=0
a=30
def draw_dot(size_gap):
    tim.hideturtle()
    global a, count_dot
    for i in range(1, 11):
        for _ in range(10):
            tim.penup()
            tim.fd(size_gap)
            tim.pendown()
            tim.color(random_color())
            tim.dot(20)
            count_dot += 1
        tim.penup()
        tim.home()
        tim.left(90)
        tim.forward(a)
        tim.right(90)
        tim.pendown()
        a += 30
    tim.shape("turtle")
    print(count_dot)
    print(a)


draw_dot(50)