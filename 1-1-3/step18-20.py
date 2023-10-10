#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    y = y + 5  # location of next floor

    # draw the floor
    for floor in range(int(num_floors)):
        rem = floor % 6
        #rim = floor % 3
        if (rem > 2):
            painter.color("yellow")
        #if (rim == 0):
            painter.color("blue")
        if (rem < 3):
            painter.color("green")
        rem = floor % 21:


    painter.pendown()
    painter.forward(100)

wn = trtl.Screen()
wn.mainloop()