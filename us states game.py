"""
1. Convert the guess to Title case (done)
* title.()

2. Check if the guess is among the 50 states (done)
* Use a for loop to through the column. If statement to check for correct name.

3. Write the correct guess onto the map (done)
* Print correct answer on screen, in right location

4. Use a loop to allow the user to keep guessing (done)
* While Loop, Flag = True, game continues and Flag = False after score = 50.

5. Record the correct guesses in a list (done)
* Create an empty list and append correct answers to it.

6. Keep track of the score  (done)
* Add to screen input, then have it change each time a correct answer is typed.

"""

import time
import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

score = 0
correct_guesses = []

all_states = pandas.read_csv("50_states.csv")

time.sleep(0.1)
screen.update()

game_is_on = True
while game_is_on:
    the_user_guess = screen.textinput(title=f"{score}/50 States Correct",
                                      prompt="What's Another State's Name? ").title()
    if the_user_guess == "Exit":
        break
    for any_state in all_states["state"]:
        if the_user_guess in correct_guesses:
            score = score   # score remains if input has already been used.
        elif the_user_guess == any_state:
            score += 1
            if score == 50:
                game_is_on = False      # game ends when user reaches 50

            correct_guesses.append(f"{the_user_guess}")     # append correct answer into list
            correct_answer_data = all_states[all_states.state == f"{the_user_guess.title()}"]   # Checks for state

            x_list = correct_answer_data["x"].to_list()     # xcor of state to list
            y_list = correct_answer_data["y"].to_list()     # ycor of state to list

            turtle.goto(x=x_list[0], y=y_list[0])           # call numbers from list as x, y
            turtle.write(f"{the_user_guess}")               # writes state on map
