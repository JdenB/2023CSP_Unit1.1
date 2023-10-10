#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spdr = trtl.Turtle()
spdr.pensize(40)
spdr.goto(0,-20)
spdr.circle(20)
lgs = 8
length = 70
distance = 360 / lgs
spdr.pensize(5)
n = 0
while (n < lgs):
  spdr.goto(0,0)
  spdr.setheading(distance*n)
  spdr.forward(length)
  spdr.right(30)
  spdr.forward(10)
  n = n + 1
spdr.hideturtle()
wn = trtl.Screen()
wn.mainloop()