
import py5
import numpy as np
from helper_functions.helpers import draw_grid
import math
import random
from turtle import *

# using turtle module for this one
# this is the equivalent of 100x100mm
# perhaps I should output 150x150mm
setup(1000,1000)



# we need a margin here to center the drawing
# where x and y are the start 
def tiling(x, y, s, l):
    if l == 0:
        # horizontal line
        if random.random() < 0.5:
            penup()
            goto(x-s,y)
            pendown()
            goto(x+s,y)    
        
        else:
            # vertical line
            penup()
            goto(x, y-s)
            pendown()
            goto(x, y+s)

        
    else:
        s /= 2
        l -= 1
        tiling(x - s, y + s, s, l)
        tiling(x + s, y + s, s, l)
        tiling(x - s, y -s, s, l)
        tiling(x + s, y -s, s, l)


hideturtle()
tracer(False)
tiling(0, 0, 400, 6)
tracer(True)
exitonclick()

