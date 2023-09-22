# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()


# ask user for a color (such as red, green, blue, pink, purple)
color = input("What color would you like your circle?\n")

# ask user for the radius of a circle
Radius = input("what radius would you like your circle\n")

# set the pen and fill colors
# then draw a circle
painter.pencolor(color)
painter.fillcolor(color)
painter.begin_fill()
painter.circle(int(Radius))
painter.end_fill()
# move the turtle to another part of the screen
painter.goto(100,100)

color2 = input("What color would you like your circle #2?\n")

# ask user for the radius of a circle
Radius2 = input("what radius would you like your circle #2?\n")

# change both the pen and fill colors
# then draw a polygon of your choice
painter.circle(100,360,5)
painter.begin_fill()
painter.end_fill()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()