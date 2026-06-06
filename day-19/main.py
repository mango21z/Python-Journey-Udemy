from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "which turtle will win the race? Enter a color:")
colors =["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

y = 150
for color in colors:
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.color(color)
    t.goto(-200,y)
    y -= 50
    all_turtle.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color}")
            else:
                print(f"You lose! {winning_color}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)












screen.exitonclick()




#turtle drawing
# def move_forwards():
#     tim.forward(10)
# def move_back():
#     tim.back(10)
# def move_left():
#     new_heading = tim.heading()+10
#     tim.setheading(new_heading)
# def move_right():
#     tim.setheading(tim.heading()-10)
#
# def clear():
#     tim.clear()
#     tim.home()
#
# screen.listen()
# screen.onkeypress(move_forwards, "w")
# screen.onkeypress(move_back, "s")
# screen.onkeypress(move_left, "a")
# screen.onkeypress(move_right, "d")
# screen.onkeypress(clear,"c")
# screen.exitonclick()
