#!/usr/bin/env python2
from cube_interactive import Cube, plt


# module globals
c, ic = None, None


def mv(face="F", turns=1, layer=0):
    """Move one layer.
    """
    c.rotate_face(face, turns, layer)
    ic._draw_cube()


def mvs(algo, debug=False):
    """Move multiple layers using an algorithm notation string.
    """
    pos, moves = -1, []
    for n, token in enumerate(str(algo)):
        # on face token
        if token in "FBUDLRMES":
            layer = 0
            if token in "MES":
                layer = 1
                if token is "M":
                    token = "L"
                elif token is "E":
                    token = "D"
                elif token is "S":
                    token = "F"
            moves.append(dict(face=token, turns=1, layer=layer))
            pos += 1
            continue
        # on two layers token
        elif token in "fbudlr":
            lay1 = dict(face=token.upper(), turns=1, layer=0)
            moves.append(lay1)
            lay2 = dict(face=token.upper(), turns=1, layer=1, second=True)
            moves.append(lay2)
            pos += 2
            continue
        # get current move to modify
        move = moves[pos]
        # on counter-clockwise token
        if token in "'i":
            move["turns"] *= -1
        # on multiplier token
        elif token.isdigit():
            move["turns"] *= int(token)
        # on unknown token
        else:
            msg = "syntax error: "
            posmsg = (" " * (n + len(msg))) + "^"
            print("{}\n{}".format(msg + algo, posmsg))
            return
        # if this is a two layer move
        if move.has_key("second"):
            other = move.copy()
            other["layer"] = moves[pos - 1]["layer"]
            # update turns
            moves[pos - 1].update(other)

        moves[pos].update(move)

    for kwargs in moves:
        if kwargs.has_key("second"):
            del kwargs["second"]
        if debug:
            print(kwargs)
        mv(**kwargs)


def mvsd(algo):
    """Like mvs() with debug enabled.
    """
    mvs(algo, debug=True)


def solve():
    """Solve the cube.
    """
    ic._solve_cube()


def so():
    """Alias for solve().
    """
    solve()


def history():
    """Show history of moves.
    """
    return c._move_list


def hi():
    """Alias for history().
    """
    return history()


def show_help():
    """Show this text.
    """
    print("""Interactive Rubik's Cube
---
Available commands:""")
    commands = [mv, mvs, mvsd, solve, so, history, hi, show_help]
    for cmd in commands:
        print("    {:<9}: {}".format(cmd.__name__, cmd.__doc__.strip()))
    print("""
Type help(<command>). to get more help on a command.
---""")


def init():
    """Create global objects and show plot.
    """
    global c, ic
    c = Cube(3)
    ic = c.draw_interactive()
    plt.show(block=False)


# initialize regardless of module role

show_help()
init()