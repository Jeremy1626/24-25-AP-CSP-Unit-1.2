# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
font_setup = ("Arial", 20, "normal")
#-----game functions--------
score_writer.penup()
score_writer.goto(-200, 200)
score_writer.hideturtle()
def change_position():
    new_xpos = rand.randint(1, 400)
    new_ypos = rand.randint(1, 300)
    spot.goto(new_xpos, new_ypos)
def update_score():
    global score
    score += 1
    score_writer.write(score, font=font_setup)
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def spot_clicked(x,y):
    spot.penup()
    change_position()
    update_score()
#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()