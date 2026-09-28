import math

def stack_height_2d(layers):
    # 0 layers = 0 height
    if layers == 0:
        return 0

    # First ball is 1 diameter tall.
    # Every extra layer adds sqrt(3) / 2.
    return 1 + (layers - 1) * math.sqrt(3) / 2
