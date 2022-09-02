import vpype_cli

vpype_cli.execute('read the_lover.svg write --pen-up the_lover_pen_up.svg')
vpype_cli.execute('read the_lover.svg linesort write --pen-up the_lover_pen_up+linesort.svg')