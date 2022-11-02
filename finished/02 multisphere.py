
import py5
import numpy as np
from helper_functions.helpers import draw_grid

# perhaps I should create the drawing first in p5js 
# then translate it to py5

def setup():    
    py5.size(378, 378, py5.SVG, 'multisphere.svg')
    # equivalent to 100mm x 100mm
    # py5.size(378, 378)
    py5.image_mode(py5.CENTER)
    py5.no_loop()
    
def draw():

    num = 120;
    radius = 200;

    # sideLength = 400;

    # paths = [];

    # py5.strokeWeight(2.5);

    for i in range(num):
      angle = py5.radians(360 / num) * i

      x1 = radius * py5.sin(angle)
      y1 = radius * py5.cos(angle)

    
    #   py5.arc(float(py5.width / 2 + x1), float(py5.height / 2 + y1), float(radius), float(0), float(2 * py5.PI))
      # py5.arc(50, 55, 50, 50, 0, py5.HALF_PI)

      py5.arc(py5.width / 2 + x1, py5.height / 2 + y1, radius, radius, 0, py5.PI * 2)
      py5.no_fill()
      
      py5.clip(0, 0, 378, 378)



    #   context.lineWidth = 4;
    #   context.strokeStyle = "white";
    #   context.stroke();

py5.run_sketch()