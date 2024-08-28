from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
# timmy_the_turtle.shape("square")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# def draw_shapes(num):
#     angle = 360/num
#     for _ in range(num):
#         timmy.forward(120)
#         timmy.right(angle)
#
# for b in range(3, 11):
#     draw_shapes(b)

#thickness, speedup, move in random directions,



#timmy.speed(9)
# timmy.forward(120)
# timmy.right(90)
# timmy.forward(120)
# timmy.forward(100)


# for it move in random directions#
# def move_random():
#     list= [0, 90, 180, 270]
#     colors = [
#         'aliceblue',
#         'antiquewhite',
#         'aqua',
#         'aquamarine',
#         'azure',
#         'beige',
#         'bisque',
#         'blanchedalmond',
#         'blueviolet',
#         'brown'
#     ]
#     directions = []
#     for _ in range(200):
#         timmy.speed("fastest")
#         timmy.pensize(15)
#         timmy.color(random.choice(colors))
#         timmy.forward(30)
#         timmy.setheading(random.choice(list))
#
#
#
# move_random()
#draw circle
screen.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
angle = [0, 90, 180, 270]
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colour = (red, green, blue)
    return colour

def draw_circles(num_of_gap):
    for _ in range(int(360 / num_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(num_of_gap)


draw_circles(10)
#change tilt

screen.exitonclick()