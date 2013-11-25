# coding: utf-8
#
# Interactive console helper for MagicCube

from cube_interactive import Cube, plt
import algos


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
        if token is " ":
            continue
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
            moves.append(dict(face=token.upper(), turns=1, layer=0))
            moves.append(dict(face=token.upper(), turns=1, layer=1, multi=1))
            pos += 2
            continue
        elif token in "xyz":
            f = ""
            if token is "x":
                f = "R"
            elif token is "y":
                f = "U"
            elif token is "z":
                f = "F"
            moves.append(dict(face=f, turns=1, layer=0))
            moves.append(dict(face=f, turns=1, layer=1, multi=1))
            moves.append(dict(face=f, turns=1, layer=2, multi=2))
            pos += 3
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
        # if this is a multi-layer move
        if move.has_key("multi"):
            multi = move["multi"]
            if 0 < multi:
                # update other layers
                for m in range(1, multi + 1):
                    other = move.copy()
                    other["layer"] = moves[pos - m]["layer"]
                    moves[pos - m].update(other)
        # update current move
        moves[pos].update(move)

    for kwargs in moves:
        if kwargs.has_key("multi"):
            del kwargs["multi"]
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
    print("""Interactive Console for Magic Cube

Available commands:""")

    commands = [mv, mvs, mvsd, solve, so, history, hi, show_help]
    for cmd in commands:
        print("    {:<9}: {}".format(cmd.__name__, cmd.__doc__.strip()))
    print("""
You can access a library of algorithms using the algos module (type: `dir(algos)`)

Type `help(<command>)` to get more help on a command.
---""")


def init():
    """Create global objects and show plot.
    """
    global c, ic
    c = Cube(3)
    ic = c.draw_interactive()
    plt.show(block=False)


if __name__ == "__main__":
    show_help()
    init()
