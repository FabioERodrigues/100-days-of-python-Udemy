import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

data = pandas.read_csv("50_states.csv")
is_continue = True
states = data["state"].tolist()
is_continue = True
guessed_states = []
while is_continue:
    answer_state = screen.textinput(title=f"Guess the state {score}", prompt="What's another state's name?").title()
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(answer_state)
        score += 1
        guessed_states.append(answer_state)

    elif answer_state == "Exit":
        #missed_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        missed_states = [state for state in states if state not in guessed_states]
        data2 = pandas.DataFrame(missed_states)
        data2.to_csv("missed_states.csv")
        #print(missed_states)
        break

    elif score == 50:
        screen.textinput(title="Result", prompt="You won").title()
        is_continue = False
        #urtle.mainloop()

    # else:
    #     answer_state = screen.textinput(title=f"Guess the state {score}", prompt="What's another state's name?")

screen.exitonclick()