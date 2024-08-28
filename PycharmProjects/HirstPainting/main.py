import random
#timport colorgram
import turtle as tur

# def random_color():
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     colour = (red, green, blue)
#     return colour
# rgb_col = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_col.append(new_color)
# print(rgb_col)
color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
turtle = tur.Turtle()
screen = tur.Screen()
tur.colormode(255)

#how to draw thr dots
# turtle.penup()
# turtle.dot()
# turtle.fd(100); turtle.dot(20, "blue"); turtle.fd(50)
# turtle.dot()

#move in 10x10 pattern
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)



for line in range(1, 101):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if line % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

#use color list to fill the dots
screen.exitonclick()