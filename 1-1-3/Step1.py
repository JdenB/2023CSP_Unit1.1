#   a113_forward_and_right.py
import turtle as trtl

painter = trtl.Turtle()
for numbers in range(6):
    painter.forward(10)
    painter.right(10)
    painter.right(10)
    painter.forward(10)
    painter.right(10)
    painter.right(10)
    painter.forward(10)
    painter.right(10)
    painter.right(10)

wn = trtl.Screen()
# END SEGMENT HERE




 #   a113_square.py
#   Write code to draw a square.

painter = trtl.Turtle()

# Your code here
painter.pu
painter.goto(-50,-50)
painter.pd
for numbers in range(4):
    painter.forward(40)
    painter.right(90)


wn = trtl.Screen()
wn.mainloop()
# END SEGMENT HERE




wn.mainloop()
#   a113_octagon.py
#   Write code that draws an octagon starting
#   at -50, 100 to leave enough room for the drawing

painter = trtl.Turtle()

# new starting location so the entire
# octagon is visible
painter.penup()
painter.goto(-50, 150)
painter.pendown()

# Your code here

wn = trtl.Screen()
wn.mainloop()