def gps(s, x):
    if len(x) <= 1:
        return 0

    speeds = []

    for i in range(1, len(x)):
        distance = x[i] - x[i - 1]

        speed = (3600 * distance) / s

        speeds.append(speed)

    return int(max(speeds))
