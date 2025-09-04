from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title('Us state guessing game')
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []

while len(guessed) < 50:
    answer = screen.textinput(f'{len(guessed)}/50 Guess the states',
                              'type the names of the states').title()
    if answer == 'Exit':
        unguessed_states = [index for index in all_states if (index not in guessed)]  # list comprehension
        d = pandas.DataFrame(unguessed_states)
        d.to_csv('unguessed_states')
        break

    if answer in all_states:
        if answer not in guessed:
            guessed.append(answer)
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data['state'] == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer, align='center', font=('arial', 10, 'normal'))

