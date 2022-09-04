import py5
# jupyter notebooks so I can display the sketch in browser?


def setup():
    # py5.size(600, 600, py5.SVG, '02.svg') 
    py5.size(600, 600)
    py5.background(255, 255, 255)
    py5.rect_mode(py5.CENTER)
    py5.no_loop()

    global img
    img = py5.create_graphics(py5.width, py5.height)
    
    global mk
    mk = py5.create_graphics(py5.width, py5.height)

def draw():
    py5.background(220);

    img.begin_draw()
    img.stroke_weight(0.5)
    img.stroke(255)
    img.smooth()
    img.no_fill(); # apply styles to new graphics layer
    img.translate(100, 100); # apply translations to new graphics layer
    
    for i in range(20):
        circleX = py5.random(2, 50)
        circleY = py5.random(2, 50)
        img.ellipse(circleX, circleY, 100, 100) #apply shapes to new graphics layer

    img.end_draw()

    mk.begin_draw()
    mk.translate(75, 75)
    mk.ellipse(0, 0, 100, 100)
    mk.end_draw()

    img_clone = img.get()
    img_clone.mask(mk.get())

    py5.image(img_clone, 0, 0)


py5.run_sketch()