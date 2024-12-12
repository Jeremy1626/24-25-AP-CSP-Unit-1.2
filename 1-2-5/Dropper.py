# Initialization of turtles and images
import turtle as trtl
import random as rand

apple_image = "apple.gif"
basket_image = "basket.gif"
xcor = 0
ycor = 50
ground_height = -200

wn = trtl.Screen()
wn.setup(width=2, height=2)
#make screen aware of new files
wn.addshape(apple_image)
wn.addshape(basket_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

basket = trtl.Turtle()
basket.penup()

def draw_apple(active_apple):
    active_apple.shape(apple_image)
    apple.showturtle()
    wn.update()

def draw_basket(active_basket):
    active_basket.shape(basket_image)
    basket.showturtle()
    wn.update()

def drop_apple():
    wn.tracer(True)
    apple.goto(xcor, ground_height)
    apple.clear()
    apple.hideturtle()


def basket_left():
    basket.goto(-200,basket_height )

def basket_right():
    basket.goto(200,basket_height)

def basket_move_left():
    if ("a" in direction_list):
        basket_left()
def basket_move_right():
    if ("d" in direction_list):
        basket_right()


draw_apple(apple)
draw_basket(basket)
drop_apple()

wn.listen()
wn.mainloop()