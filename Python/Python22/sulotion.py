import math

def find_next_square(sq):
    root = int(math.sqrt(sq))

    if root * root != sq:
        return -1

    return (root + 1) ** 2
