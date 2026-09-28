def array_packing(a):
    M = 0

    for i in range(len(a)):
        M |= a[i] << (8 * i)

    return M
