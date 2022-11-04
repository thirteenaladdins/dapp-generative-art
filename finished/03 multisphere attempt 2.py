
import py5
import numpy as np
from helper_functions.helpers import draw_grid
import math

# perhaps I should create the drawing first in p5js 
# then translate it to py5

def setup():    
    py5.size(378, 378, py5.SVG, 'multisphere_2.svg')
    # equivalent to 100mm x 100mm
    py5.size(378, 378)
    # py5.size(1080,1080)
    py5.image_mode(py5.CENTER)
    py5.no_loop()
    
def draw():

    # scale this to fit in the canvas
    num = 120;
    radius = 80;
    
    # sideLength = 400;

    # paths = [];

    # py5.strokeWeight(2.5);

    for i in range(0, num, 2):
      angle = math.radians(360 / num) * i

      x1 = radius * math.sin(angle)
      y1 = radius * math.cos(angle)

    
      # py5.arc(float(py5.width / 2 + x1), float(py5.height / 2 + y1), float(radius), float(radius), float(2 * py5.PI))
      # py5.arc(50, 55, 50, 50, 0, py5.HALF_PI)

        # its like cracking a puzzle


    #   py5.begin_shape()
      py5.ellipse_mode(py5.RADIUS)
    #   py5.arc(py5.width / 2 + x1, py5.height / 2 + y1, radius, radius,  0,  py5.PI * 2)
      py5.ellipse(py5.width / 2 + x1, py5.height / 2 + y1, radius, radius)
      py5.no_fill()
      
      # py5.clip(0, 0, 378, 378)

    #   context.lineWidth = 4;
    #   context.strokeStyle = "white";
    #   context.stroke();

py5.run_sketch()