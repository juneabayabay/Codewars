def calc_tip(p, r): # we define a function to calculate the tip based on the price and the rating
    rounded = ((p + 5) // 10) * 10

    T = rounded // 10

    if r == 1:
        T += 1
    elif r == 0:
        T -= 1
    elif r == -1:
        T = (T // 2) - 1

    return max(0, T)