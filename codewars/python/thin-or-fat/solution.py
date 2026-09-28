import math

def thin_or_fat(matrix):
    # Calculate Widths (sum of each row)
    widths = [sum(row) for row in matrix]

    # Calculate Heights (sum of each column)
    heights = []

    for col in range(len(matrix[0])):
        column_sum = sum(row[col] for row in matrix)
        heights.append(column_sum)

    # If any Width or Height is negative, return None
    if any(x < 0 for x in widths) or any(x < 0 for x in heights):
        return None

    # Sum of square roots of Widths
    width_total = sum(math.sqrt(x) for x in widths)

    # Sum of square roots of Heights
    height_total = sum(math.sqrt(x) for x in heights)

    # Check if they are approximately equal
    if abs(width_total - height_total) < 1e-10:
        return "perfect"

    # Width is bigger
    if width_total > height_total:
        return "fat"

    # Height is bigger
    return "thin"
