# coding: utf-8
#
# Interactive console helper for MagicCube

import random
from cube_interactive import Cube, plt
import algos


# module globals
c, ic = None, None


def mv(face="F", turns=1, layer=0, dontdraw=False):
    """Move one layer.
    """
    c.rotate_face(face, turns, layer)
    if not dontdraw:
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

    for n, kwargs in enumerate(moves):
        if kwargs.has_key("multi"):
            del kwargs["multi"]
        if debug:
            print(kwargs)
        mv(dontdraw=(n < (len(moves) - 2)), **kwargs)

    return algo


def mvsd(algo):
    """Like mvs() with debug enabled.
    """
    return mvs(algo, debug=True)


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


def scramble(moves=23):
    """Scramble the cube in the given number of moves.
        :param moves: Maximum number of moves (default: 23)
    """
    if moves < 1:
        raise ValueError("moves must be greater than zero")
    FACES = "FBUDLR"
    algo = ""
    move_ct = 0
    while move_ct < moves:
        face = random.choice(FACES)
        # add face
        algo += face
        if random.gauss(1, 0.5) < 1.0:
            # add random number
            x = random.randint(2, 3)
            if moves < (move_ct + x):
                if move_ct < (moves - 1):
                    move_ct += 1
                    continue
                else:
                    break
            algo += str(x)
            move_ct += x
        if random.gauss(1, 10) < 7:
            # add invert move
            algo += "'"
        move_ct += 1

    return mvs(algo)


def sc(moves=23):
    """Like scramble(), but solves the cube before scrambling.
    """
    solve()
    return scramble(moves)


def show_help():
    """Show this text.
    """
    commands = [mv, mvs, mvsd, solve, so, history, hi, scramble, sc, show_help]
    txt = ["""Interactive Console for Magic Cube

Available commands:"""]
    txt += ["    {:<9}: {}".format(cmd.__name__, cmd.__doc__.strip()) for cmd in commands]
    txt.append("""
You can access a library of algorithms using the algos module (type: `dir(algos)`)

Type `help(<command>)` to get more help on a command.
---""")
    print("\n".join(txt))


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
