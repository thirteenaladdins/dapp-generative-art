import py5
import math 
from random import randint, randrange

def setup():
  py5.size(577, 577)
  py5.size(577, 577, py5.SVG, 'uncalibrated.svg')
  py5.no_loop()


def draw():
  # py5.background(220)
  
  # py5.square(x + y * z, x, 30, 30 )

  py5.square(20,20, 30 )
  for x in range(20, py5.width - 40, randrange(1, 16)):
      for y in range(20, py5.height - 40, randrange(1, 16)):
        for z in range(0, py5.height - 40, 4):
              
          if (x + (y * z) + 30 < py5.width - 20): 
            py5.no_fill()
            py5.square(x + y * z, x, 30 )
            
  for x in range(20, py5.width - 40, randrange(1, 16)):
      for y in range(20, py5.height - 40, randrange(1, 16)):
        for z in range(0, py5.height - 40, 4):
              
          if (x + (y * z) + 30 < py5.width - 20): 
            py5.no_fill()
            py5.square(x, x + y * z, 30 )
    
py5.run_sketch()