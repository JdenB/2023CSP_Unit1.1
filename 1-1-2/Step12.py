# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color = input("What color would you like your circle?\n")

# ask user for the radius of a circle
Radius = input("what radius would you like your circle\n")

# ask user how thicc they want their line to be :3
Thiccness = input("how dummy thick do you want your circles line\n")


# ask user if they want their circle filled or no :3


# draw a circle with the radius and line color entered by the user
painter.pensize(Thiccness)
painter.pencolor(color)
painter.circle(float(Radius))

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()