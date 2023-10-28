import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states_df = pd.read_csv("50_states.csv")
states_list = states_df["state"].to_list()

score = 0
answered_states = []

while score <= len(states_list):
    user_answer = turtle.textinput(title=f"{score}/{len(states_list)} States Correct", prompt="Type the name of any "
                                                                                              "state? or Type "
                                                                                              "exit").capitalize()
    if user_answer == "Exit":
        states_not_answered = {
            "State": [state for state in states_list if state not in answered_states]
        }
        states_not_answered_df = pd.DataFrame(states_not_answered)
        states_not_answered_df.to_csv("states_to_learn.csv")
        break

    if user_answer in states_list:
        score += 1
        curr_state = states_df[states_df.state == user_answer]
        writer.goto(int(curr_state.x.iloc[0]), int(curr_state.y.iloc[0]))
        writer.write(user_answer)
        answered_states.append(user_answer)
