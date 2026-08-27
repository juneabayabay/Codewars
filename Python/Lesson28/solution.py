def collision(x1, y1, radius1, x2, y2, radius2):
    # Find the distance between the centers
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # If the distance is smaller than the two radii added together,
    # the circles are touching or overlapping.
    if distance <= radius1 + radius2:
        return True
    else:
        return False
