import turtle as trtl

painter = trtl.Turtle()
#Mood = input("are you happy or sad\n")
color = "yellow"
color2 = "black"
painter.pencolor(color)
painter.pensize(5)
painter.fillcolor(color)
painter.begin_fill()
painter.circle(100)
painter.end_fill()
painter.penup()
painter.pencolor(color2)
painter.goto(75,100)
painter.pendown()
painter.circle(1)
painter.penup()
painter.pencolor(color2)
painter.goto(-75,100)
painter.pendown()
painter.circle(1)
painter.penup()
painter.goto(0,50)
painter.begin_poly()