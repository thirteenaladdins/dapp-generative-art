# create a new file setup in the current directory

#!/usr/bin/env python3
import os
import sys

# create a new python file in the current directory
def setup_sketch():
    # get the name of the sketch
    # sketch_name = sys.argv[1]
    sketch_name = input("Enter file name: ")
    # create the file
    # this needs to be somewhere
    with open(sketch_name + '.py', 'w') as f:
        f.write('''#!/usr/bin/env python3
import py5


def setup():
    py5.size(400, 400)

def draw():
    pass

py5.run_sketch()'''
        )


def main():
    setup_sketch()


if __name__ == "__main__":
    setup_sketch()
