import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_guess = []
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in correct_guess]
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")
        break
    elif answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_data = data[data.state == answer_state]
        t.goto(correct_data.x.item(), correct_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 7, "normal"))
        correct_guess.append(answer_state)

#state to learn



screen.exitonclick()











