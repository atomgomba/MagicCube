Magic Cube
==========

It had to happen someday.  Somebody stop me!

.. image:: http://4.bp.blogspot.com/-iruqaXDstKk/UKBejowDVkI/AAAAAAAAZkM/c2tir0qcexQ/s400/test04.png
   :alt: cube views
   :align: left


Authors
-------

- **David W. Hogg** (NYU)
- **Jacob Vanderplas** (UW)
- **Károly Kiripolszky** (STFU)
  interactive console


Usage
-----

Interactive Cube
~~~~~~~~~~~~~~~~
To use the matplotlib-based interactive cube, run 

     python code/cube_interactive.py

If you want a cube with a different number of sides, use e.g.

     python code/cube_interactive.py 5

This will create a 5x5x5 cube

This code should currently be considered to be in beta --
there are several bugs and the GUI has an incomplete set of features

To control the interactive cube using an interactive console, type

    code/console

or

   python -i code/console.py

In the console you can execute algorithms written in the Singmaster notation, e.g.

   mvs("F2B2R2L2U2D2")

There's also an algorithm library you can access using the `algos` keyword.

   # this is the same as the last example (checkers pattern)
   mvs(algos.patt.checkers)

Controls
********
- **Click and drag** to change the viewing angle of the cube.  Holding shift
  while clicking and dragging adjusts the line-of-sight rotation.
- **Arrow keys** may also be used to change the viewing angle.  The shift
  key has the same effect
- **U/D/L/R/B/F** keys rotate the faces a quarter turn clockwise.  Hold the
  shift key to rotate counter-clockwise.  Hold a number i to turn the slab
  at a depth i (e.g. for a 3x3 cube, holding "1" and pressing "L" will turn
  the center slab).

Other commands
**************

You can control the cube using python commands in the interactive console.

Use the command `mv()` to move a single layer, `mvs()` to execute a sequence
of moves (algorithm in Singmaster notation) and `mvsd()` to do the same,
but with verbose output.

To solve the cube type `solve()` (or `so()` for short), to show the history of
moves type `history()` (or `hi()` for short).

Other
~~~~~
There are more tools available -- for now, RTFSC.


License
-------

All content copyright 2012 the authors.
**Magic Cube** is licensed under the *GPLv2 License*.
See the `LICENSE.txt` file for more information.
