# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
from pickle import GLOBAL

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def change_position():
    new_xpos = rand.randint(1, 400)
    new_ypos = rand.randint(1, 300)
    spot.goto(new_xpos, new_ypos)
def update_score():
    global score
    score = score + 1
    print(score)
def spot_clicked(x,y):
    spot.penup()
    change_position()
    update_score()
#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()