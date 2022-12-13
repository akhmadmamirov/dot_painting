# import colorgram

# colors = colorgram.extract('dots.jpg', 30)

# my_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     my_colors.append(new_color)

# print(my_colors)
import turtle as t
import random
t.colormode(255)

tim = t.Turtle()
screen = t.Screen()
tim.hideturtle()
tim.penup()
tim.goto(-200, -200)
tim.speed('fastest')


list_color = [ (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
 (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), 
 (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50),
 (130, 28, 31), (184, 205, 174), (41, 60, 72),(83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), 
 (215, 177, 182), (19, 71, 63), (175, 192, 212)] 


number_dots = 100
for d in range(1, number_dots + 1):
    tim.dot(15, random.choice(list_color))
    tim.forward(50)

    if d % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    
    
    





 

screen.exitonclick()