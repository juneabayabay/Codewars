from math import isqrt
# Import isqrt() so we can find the whole-number square root of n.


def longest_sequence(n: int) -> list[int]:
    # Define a function called longest_sequence.
    # n is the number we are trying to make.
    # The function will return a list of integers.

    if n <= 0:
        # If n is 0 or negative, there is no positive sequence.
        return []
        # Return an empty list.

    best = []
    # This will store the longest sequence we find.
    # At the beginning, we have found nothing.

    left = 1
    # 'left' is the first number in our current sequence.
    # We start with 1.

    total = 0
    # 'total' stores the sum of the squares
    # in our current sequence.

    for right in range(1, isqrt(n) + 1):
        # 'right' is the last number in our sequence.
        # We increase it one number at a time.
        #
        # We only go up to sqrt(n), because any number
        # bigger than sqrt(n) would have a square bigger than n.

        total += right * right
        # Add right² to total.
        #
        # For example, if right = 4:
        # right * right = 4 * 4 = 16
        #
        # So we add 16 to total.

        while total > n and left <= right:
            # If total is bigger than n,
            # our current sequence is too large.
            #
            # Remove numbers from the beginning
            # until total is small enough.

            total -= left * left
            # Remove left² from total.
            #
            # For example, if left = 2:
            # left * left = 2 * 2 = 4
            #
            # So we subtract 4 from total.

            left += 1
            # Move the beginning of the sequence forward by 1.
            #
            # Example:
            # left = 1 becomes left = 2

        if total == n:
            # If total is exactly n,
            # we have found a valid sequence.

            sequence = list(range(left, right + 1))
            # Create the sequence from left to right.
            #
            # Example:
            # left = 3
            # right = 5
            #
            # range(3, 6) gives:
            # 3, 4, 5
            #
            # list(...) makes:
            # [3, 4, 5]

            if len(sequence) > len(best):
                # Check if this sequence is longer
                # than the best sequence we found before.

                best = sequence
                # If it is longer, save it as the new best answer.

    return best
    # After checking all possible sequences,
    # return the longest one.
