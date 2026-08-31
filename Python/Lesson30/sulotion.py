def alphabet_war(fight):
    left = {"w": 4, "p": 3, "b": 2, "s": 1}
    right = {"m": 4, "q": 3, "d": 2, "z": 1}

    # Remove letters next to bombs
    alive = ""

    for i in range(len(fight)):
        if fight[i] == "*":
            continue

        # Check if the letter is next to a bomb
        if i > 0 and fight[i - 1] == "*":
            continue

        if i < len(fight) - 1 and fight[i + 1] == "*":
            continue

        alive += fight[i]

    left_power = 0
    right_power = 0

    for letter in alive:
        if letter in left:
            left_power += left[letter]

        if letter in right:
            right_power += right[letter]

    if left_power > right_power:
        return "Left side wins!"
    elif right_power > left_power:
        return "Right side wins!"
    else:
        return "Let's fight again!"
