def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)









