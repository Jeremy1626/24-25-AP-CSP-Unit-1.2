import turtle as trtl
score_writer = trtl
score = 0


spot = trtl.Turtle()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)

box = trtl.Turtle()
box.goto(100,0)
box.shape("square")
box.shapesize(3)

def update_score_for_spot(x, y, ):
  global score
  score = score + 1
  print(score)

def update_score_for_box(x,y):
  global score
  score = score + 1
  print(score)


#---------events----------
spot.onclick(update_score_for_spot)
box.onclick(update_score_for_box)
wn = trtl.Screen()
wn.mainloop()
