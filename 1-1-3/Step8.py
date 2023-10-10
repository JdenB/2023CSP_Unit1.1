#   a113_circle_of_circles.py
#   Modify this code to draw a circle of circles
import turtle as trtl

painter = trtl.Turtle()
for numbers in range(8):
    painter.shape("circle")
    painter.circle(90)
    painter.forward(50)
    painter.right(45)
wn = trtl.Screen()
wn.mainloop()
