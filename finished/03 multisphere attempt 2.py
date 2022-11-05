
import py5
import numpy as np
from helper_functions.helpers import draw_grid
import math

def setup():    
    py5.size(378, 378, py5.SVG, 'multisphere_2.svg')
    # equivalent to 100mm x 100mm
    py5.size(378, 378)
    py5.image_mode(py5.CENTER)
    py5.no_loop()
    
def draw():

    # scale this to fit in the canvas
    num = 120;
    radius = 80;

    py5.rect(0, 0, py5.width, py5.height)
    
    for i in range(0, num, 2):
      angle = math.radians(360 / num) * i

      x1 = radius * math.sin(angle)
      y1 = radius * math.cos(angle)


      py5.ellipse_mode(py5.RADIUS)
      py5.ellipse(py5.width / 2 + x1, py5.height / 2 + y1, radius, radius)
      py5.no_fill()
      

py5.run_sketch()