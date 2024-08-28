# from turtle import Turtle, Screen
#
#
# angelo = Turtle()
# print(angelo)
# angelo.shape("turtle")
# angelo.color("blue4")
# angelo.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from lprettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",
["Pikachu","Squirtle","Charmander"])

table.add_column("Type",
["Electric","Water","Fire"])

print(table)