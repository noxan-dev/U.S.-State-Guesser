import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


data = pandas.read_csv("50_states.csv")
data_state_list = data.state.to_list()
already_guessed = []


while len(already_guessed) < 50:
    user_guess = screen.textinput(title=f"Guess the state {len(already_guessed)}/50",
                                  prompt="What's another states name?").title()
    coordinates = data[data.state == user_guess]
    if user_guess in already_guessed:
        print('Already guessed, try again.')
    elif user_guess == "Exit":
        missing_states = []
        for state in data_state_list:
            if state not in already_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states, columns=['state'])
        new_data.to_csv("states_to_learn.csv")
        break
    elif user_guess in data_state_list:
        already_guessed.append(user_guess)
        t = turtle.Turtle()
        t.ht()
        t.pu()
        t.goto(int(coordinates.x), int(coordinates.y))
        t.write(user_guess, move=False, font=("Arial", 10, "normal"))


missed_data = pandas.read_csv("states_to_learn.csv")
missed_data_list = missed_data.state.to_list()
for state in missed_data_list:
    m_coordinates = data[data.state == state]
    m = turtle.Turtle()
    m.pu()
    m.ht()
    m.color("red")
    m.goto(int(m_coordinates.x), int(m_coordinates.y))
    m.write(state, move=False, font=("Arial", 10, "normal"))


screen.exitonclick()
