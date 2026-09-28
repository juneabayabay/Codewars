"""Quick logic test for tic tac toe cell mapping."""

def click_to_cell(x, y):
    if x < -3 or x > 3 or y < -3 or y > 3:
        return None, None
    col = min(2, max(0, int((x + 3) // 2)))
    if x == 3:
        col = 2
    row = min(2, max(0, int((3 - y) // 2)))
    if y == -3:
        row = 2
    return row, col


def key_to_cell(index):
    return index // 3, index % 3


def cell_xy(i, j):
    return 2 * (j - 1), -2 * (i - 1)


# Key layout should match visual centers
centers = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}

for key in range(1, 10):
    row, col = key_to_cell(key - 1)
    assert (row, col) == centers[key], f"key {key}: got {(row,col)} expected {centers[key]}"

for key, (row, col) in centers.items():
    x, y = cell_xy(row, col)
    r2, c2 = click_to_cell(x, y)
    assert (r2, c2) == (row, col), f"click center ({x},{y}) -> {(r2,c2)} expected {(row,col)}"

print("All mapping tests passed.")
