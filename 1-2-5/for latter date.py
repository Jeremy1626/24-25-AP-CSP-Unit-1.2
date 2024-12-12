def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)






def reset_apple (apple):
    if apple < ground_height:
        newx = rand.randint(-200, 200)
        newy = 0
        apple.goto(newx, newy)


drop_apple()