# import run server?
# so here's my plan - instead of adding a module that outputs to the browser
# I will instead create the work in p5js and then convert the code to python
# when I need to output it to SVG
# I don't like this approach but I'm not sure how else to do it

import py5

grid_width = 20
grid_height = 20
grid_spacing = 1

def mouse_pressed():
    py5.end_record()
    py5.exit_sketch()

def setup():
    # py5.size(1080, 1080, py5.SVG, 'first_drawing.svg')
    py5.size(1080, 1080)
    # output to canvas
    # there is no usable workflow here
    py5.begin_record(py5.SVG, 'first_drawing.svg')
    py5.no_loop()

def draw():
    create_grid(grid_width, grid_height, grid_spacing)


def create_grid(grid_width, grid_height, grid_spacing):
    for x in range(grid_width):
        for y in range(grid_height):

            # TODO grid spacing is not working
            #             
            py5.no_stroke()

            # randomise the colours here
            py5.fill(255, 0, 0)
            py5.rect(x * grid_spacing, y * grid_spacing, grid_spacing, grid_spacing)
            # py5.rect(x, y, grid_spacing, grid_spacing)
            

py5.run_sketch()
# py5.exit_sketch()
