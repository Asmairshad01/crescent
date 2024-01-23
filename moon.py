import turtle as t
t.title("for bestie")

t.bgcolor('black')
t.up()
t.goto(0, -200)
t.begin_fill()
t.color('yellow')
t.circle(200)
t.end_fill()

t.up()
t.goto(-50, -200)
t.begin_fill()
t.color('black')
t.circle(200)
t.end_fill()

t.up()
t.setpos(-130, -10)
t.down()
t.color("white")
t.write("TO THE MOON>>>", font=("rockwell nova", 23, "bold"))

t.up()
t.setpos(-130, -110)
t.down()
t.color("black")
t.write("TO THE MOON>>", font=("rockwell nova", 20, "bold"))

t.ht()

t.mainloop()

