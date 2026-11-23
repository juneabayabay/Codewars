def give_change(amount):
    bills = [1, 5, 10, 20, 50, 100]
    result = [0, 0, 0, 0, 0, 0]

    for i in range(len(bills) - 1, -1, -1):
        result[i] = amount // bills[i]
        amount = amount % bills[i]

    return tuple(result)
