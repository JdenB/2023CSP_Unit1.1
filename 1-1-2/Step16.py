# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(10)

# move the turtle to another part of the screen
painter.penup()
painter.goto(5,9)
painter.pendown()
painter.circle(100,180,1)

# add code here for an arc
painter.circle(100,180,1)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-10,-9)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(100,180,5)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-3,-1)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(100,360,50)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()