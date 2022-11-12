import vpype_cli
import sys

# input from command line

if len(sys.argv) < 2:
    print("Usage: python vpype_optimisation.py <filename>")
    sys.exit(1)

else:
    input_file = sys.argv[1]



# vpype_cli.execute('read the_lover.svg write --pen-up the_lover_pen_up.svg')
# vpype_cli.execute('read the_lover.svg linesort write --pen-up the_lover_pen_up+linesort.svg')


vpype_cli.execute(f'read {input_file} scaleto 15cm 15cm linesort write --page-size 15x15cm --center {input_file}_output')
