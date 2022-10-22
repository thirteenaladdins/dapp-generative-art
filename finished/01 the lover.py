import py5
import py5_tools
# import time


# py5 size?
# output in millimetres
# py5_tools.set_py5_size(100, 100, 'mm')

def setup():
    
    
    py5.size(600, 600, py5.SVG, 'the_lover.svg')
    # py5.size(600, 600)
    py5.no_loop()
    
# this outputs the shape I want but it doesn't create a suitable 
# file to convert to gcode
# output 

def draw():    
    py5.stroke_weight(2.5)    
    num = 120
    radius = 150
    py5.translate(py5.width / 2, py5.height / 2)
    py5.no_fill()
    
    for i in range(num):
        angle = py5.radians(360 / num) * i
        x1 = radius * py5.sin(angle)
        y1 = radius * py5.cos(angle)

        py5.arc(x1, y1, radius, radius, 0, py5.PI)

py5.run_sketch()


