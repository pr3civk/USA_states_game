import turtle as t
import pandas as pd
import time


def get_mouse_click_coor(x, y):
    print(x, y)


# def clock():
#     for s in range(600, 0, -1):
#         seconds = s % 60
#         minutes = int(s / 60) % 60
#         time.sleep(1)
#         return(f"{minutes} : {seconds}")


image = "../Python/US_STATES_GAME/blank_states_img.gif"


screen = t.Screen()
screen.title("U.S.States Game")
screen.setup(725, 491)

screen.addshape(image)


t.shape(image)
t.onscreenclick(get_mouse_click_coor)

us_map = pd.read_csv("../Python/US_STATES_GAME/50_states.csv")
us_states = us_map.state.to_list()
us_states_coor = dict(zip(us_map["state"], zip(us_map["x"], us_map["y"])))


s = t.Turtle()
s.speed(0)
s.hideturtle()
s.pu()


n = 0
answers = []
while True:
    answer_state = screen.textinput(
        title=f"{n}/50 States Correct", prompt="What's another state's name?"
    ).title()
    if answer_state in us_states and answer_state not in answers:
        s.goto(us_states_coor[answer_state])
        s.write(answer_state, font=("Arial", 10, "bold"))
        n += 1
        answers.append(answer_state)
    elif answer_state in ["E", "Exit"]:
        print("--- exit --- " * 8)
        break
    else:
        continue
    if n == 50:
        s.goto(-200, 0)
        s.write("YOU HAVE WON!", font=("Arial", 40, "bold"))



not_guessed_states = [s for s in us_states if s not in answers]
data2 = pd.DataFrame(not_guessed_states)
data2.to_csv("../Python/US_STATES_GAME/states.csv")
print(data2)


            


t.mainloop()
