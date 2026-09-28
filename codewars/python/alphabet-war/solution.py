def alphabet_war(fight):
    # Start both sides with 0 power
    left = 0
    right = 0

    # Check every letter in the fight string
    for letter in fight:

        # Left side letters
        if letter == "w":
            left += 4
        elif letter == "p":
            left += 3
        elif letter == "b":
            left += 2
        elif letter == "s":
            left += 1

        # Right side letters
        elif letter == "m":
            right += 4
        elif letter == "q":
            right += 3
        elif letter == "d":
            right += 2
        elif letter == "z":
            right += 1

    # Compare the power of both sides
    if left > right:
        return "Left side wins!"
    elif right > left:
        return "Right side wins!"
    else:
        return "Let's fight again!"
