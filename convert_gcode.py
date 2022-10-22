
import svgpathtools
import sys     

# import svg file from command line
svg_file = sys.argv[1]

svg = svgpathtools.svg2paths(svg_file)
print(svg)

# convert svg paths to gcode
# def convert_svg_to_gcode(svg_file):

# for each path 
# Path(Arc(start=(75+150j), radius=(75+75j), rotation=0.0, large_arc=False, sweep=True, end=(-75+150j)))

# that path should be a simple arc

# convert path to gcode

