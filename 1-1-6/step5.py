#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
  #Spdr is the name of turtle, (spdr representing spider)
spdr = trtl.Turtle()
spdr.pensize(40)
spdr.goto(0,-20)
spdr.circle(20)
  #Code below sets configuration of the legs
drawn = 0
lgs = 8
length = 70
distance = 360 / lgs
spdr.pensize(5)
  #The following portion of code draws legs
n = 0
spdr.setheading(distance * n -45)
while (n < lgs):
  while (n <= 3):
    spdr.setheading(distance * n + 45)
    spdr.goto(0, 0)
    spdr.setheading(distance * n)
    spdr.forward(length)
    n = n + 1
    drawn = drawn + 1
  while (n <= 6):
    spdr.penup()
    n + 2
    spdr.goto(0, 0)
    spdr.setheading(distance * n)
    spdr.forward(length)
    spdr.pendown()
  while (n <= 8):
    spdr.setheading(distance * n + 45)
    spdr.goto(0, 0)
    spdr.setheading(distance * n)
    spdr.forward(length)
    n = n + 1
    drawn = drawn + 1


spdr.hideturtle()
wn = trtl.Screen()
wn.mainloop()