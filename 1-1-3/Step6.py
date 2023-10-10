import turtle as trtl

painter = trtl.Turtle()
#   a113_square.py
#   Write code to draw a square.



# Your code here
painter.pu()
painter.goto(-50,-50)
painter.pd()
for numbers in range(4):
    painter.forward(40)
    painter.right(90)


wn = trtl.Screen()
wn.mainloop()
# END SEGMENT HERE



for numbers in range(8):
    painter.forward(8)
    painter.right(45)