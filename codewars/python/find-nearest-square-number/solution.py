def nearest_sq(n):
    root = int(n ** 0.5)

    lower_square = root ** 2
    upper_square = (root + 1) ** 2

    if n == lower_square:
        return n

    if n - lower_square < upper_square - n:
        return lower_square
    else:
        return upper_square
