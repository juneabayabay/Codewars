"""
============================================================
                 STONE TIC TAC TOE
============================================================

HOW TO PLAY
-----------

Keyboard:

        1 | 2 | 3
       ---+---+---
        4 | 5 | 6
       ---+---+---
        7 | 8 | 9

Press 1-9 to place a piece.

You can also CLICK directly on a cell.

Press R to restart the game.

RULES
-----

X and O take turns.

A player wins by getting three pieces in a row:

    - Horizontal
    - Vertical
    - Diagonal

If all nine cells are filled and nobody wins,
the game ends in a tie.

============================================================
"""

import turtle


# ============================================================
#                         COLORS
# ============================================================

BACKGROUND = "#55564E"

STONE = "#99998B"
STONE_LIGHT = "#A8A596"
STONE_DARK = "#6A695F"

GRID = "#383934"
GRID_HIGHLIGHT = "#74736A"

PIECE = "#C1BBAA"
PIECE_LIGHT = "#D8D2C2"
PIECE_DARK = "#716B61"

TEXT = "#F1EEE5"
TEXT_SECONDARY = "#C9C5B8"

WIN_COLOR = "#D6C27A"


# ============================================================
#                      SCREEN SETTINGS
# ============================================================

screen = turtle.Screen()

screen.setup(width=900, height=900)
screen.title("Stone Tic Tac Toe")

# Coordinate system:
#
#                 +Y
#                  |
#                  |
#          --------+-------- +X
#                  |
#                  |
#
# The visible world goes from -5 to +5.
screen.setworldcoordinates(-5, -5, 5, 5)

screen.bgcolor(BACKGROUND)

# Disable automatic Turtle animation.
# We will manually update the screen.
screen.tracer(0, 0)


# ============================================================
#                       TURTLE OBJECTS
# ============================================================

# Main drawing turtle.
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Text turtle.
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)

# Separate turtle for the winning line.
win_pen = turtle.Turtle()
win_pen.hideturtle()
win_pen.speed(0)


# ============================================================
#                       GAME STATE
# ============================================================

# Board representation:
#
#     0 = empty
#     1 = X
#     2 = O
#
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# X starts.
turn = "X"

# Becomes True after a win or tie.
game_over = False

# Number of successful moves.
move_count = 0

# Message displayed to the player.
current_message = "X's turn"

# Cells that form the winning line.
winning_cells = []


# ============================================================
#                   BOARD GEOMETRY
# ============================================================

# The actual playable board is:

BOARD_LEFT = -3
BOARD_RIGHT = 3
BOARD_BOTTOM = -3
BOARD_TOP = 3

# Each cell is exactly 2 x 2 units.

CELL_SIZE = 2

# Centers of the cells:
#
#       -2    0    2
#
# y=2   1    2    3
# y=0   4    5    6
# y=-2  7    8    9

CELL_CENTERS = [-2, 0, 2]


# ============================================================
#                BOARD POSITION CONVERSION
# ============================================================

def cell_center(row, col):
    """
    Convert a board row and column into
    the exact center coordinate of that cell.

    Example:

        (0, 0) -> (-2, 2)
        (0, 1) -> ( 0, 2)
        (0, 2) -> ( 2, 2)

        (1, 0) -> (-2, 0)
        (1, 1) -> ( 0, 0)
        (1, 2) -> ( 2, 0)

        (2, 0) -> (-2,-2)
        (2, 1) -> ( 0,-2)
        (2, 2) -> ( 2,-2)
    """

    x = CELL_CENTERS[col]
    y = CELL_CENTERS[2 - row]

    return x, y


def number_to_cell(number):
    """
    Convert a number from 1-9 into
    a row and column.

    Examples:

        1 -> (0, 0)
        5 -> (1, 1)
        9 -> (2, 2)
    """

    index = number - 1

    row = index // 3
    col = index % 3

    return row, col


# ============================================================
#                    DRAW STONE BOARD
# ============================================================

def draw_stone_slab():
    """
    Draw the large stone slab behind the board.
    """

    pen.clear()

    pen.penup()

    # Start at upper-left.
    pen.goto(-3.55, 3.55)

    pen.setheading(0)

    # Dark outer border.
    pen.color(STONE_DARK, STONE_DARK)

    pen.begin_fill()

    for _ in range(4):
        pen.forward(7.1)
        pen.right(90)

    pen.end_fill()

    # Inner stone.
    pen.goto(-3.40, 3.40)

    pen.color(STONE_LIGHT, STONE)

    pen.begin_fill()

    for _ in range(4):
        pen.forward(6.8)
        pen.right(90)

    pen.end_fill()

    pen.penup()


# ============================================================
#                     DRAW BOARD GRID
# ============================================================

def draw_board():
    """
    Draw the four lines that create
    the nine Tic Tac Toe cells.
    """

    # --------------------------------------------------------
    # Slight shadow underneath the grooves
    # --------------------------------------------------------

    pen.pensize(12)
    pen.pencolor(GRID_HIGHLIGHT)

    # Horizontal shadow lines.
    for y in (-1, 1):

        pen.penup()
        pen.goto(-3, y - 0.02)
        pen.setheading(0)

        pen.pendown()
        pen.forward(6)

    # Vertical shadow lines.
    for x in (-1, 1):

        pen.penup()
        pen.goto(x + 0.02, -3)
        pen.setheading(90)

        pen.pendown()
        pen.forward(6)

    # --------------------------------------------------------
    # Main dark grooves
    # --------------------------------------------------------

    pen.pensize(8)
    pen.pencolor(GRID)

    # Horizontal lines.
    for y in (-1, 1):

        pen.penup()
        pen.goto(-3, y)
        pen.setheading(0)

        pen.pendown()
        pen.forward(6)

    # Vertical lines.
    for x in (-1, 1):

        pen.penup()
        pen.goto(x, -3)
        pen.setheading(90)

        pen.pendown()
        pen.forward(6)

    pen.penup()


# ============================================================
#                         DRAW X
# ============================================================

def draw_stone_x(x, y):
    """
    Draw a centered stone X.

    The X has:
        1. dark shadow
        2. lighter inner stroke

    IMPORTANT:
    We explicitly set the Turtle heading before every
    diagonal line so the drawing is always predictable.
    """

    size = 0.62

    # --------------------------------------------------------
    # Shadow
    # --------------------------------------------------------

    pen.pensize(13)
    pen.pencolor(PIECE_DARK)

    # First diagonal.
    pen.penup()
    pen.goto(x - size, y - size)
    pen.setheading(45)

    pen.pendown()
    pen.forward(size * 2 * 1.414)

    # Second diagonal.
    pen.penup()
    pen.goto(x - size, y + size)
    pen.setheading(-45)

    pen.pendown()
    pen.forward(size * 2 * 1.414)

    pen.penup()

    # --------------------------------------------------------
    # Light inner X
    # --------------------------------------------------------

    inner = 0.53

    pen.pensize(7)
    pen.pencolor(PIECE_LIGHT)

    # First diagonal.
    pen.penup()
    pen.goto(x - inner, y - inner)
    pen.setheading(45)

    pen.pendown()
    pen.forward(inner * 2 * 1.414)

    # Second diagonal.
    pen.penup()
    pen.goto(x - inner, y + inner)
    pen.setheading(-45)

    pen.pendown()
    pen.forward(inner * 2 * 1.414)

    pen.penup()


# ============================================================
#                         DRAW O
# ============================================================

def draw_stone_o(x, y):
    """
    Draw a perfectly centered stone O.

    The Turtle heading is explicitly reset to 0
    before drawing every circle.

    This fixes the alignment problem from the
    previous version.
    """

    outer_radius = 0.68
    inner_radius = 0.43

    # --------------------------------------------------------
    # Outer dark stone ring
    # --------------------------------------------------------

    pen.penup()

    # Turtle's circle is based on its current heading.
    # Setting heading to 0 guarantees consistent geometry.
    pen.setheading(0)

    pen.goto(x, y - outer_radius)

    pen.pencolor(PIECE_DARK)
    pen.pensize(5)
    pen.fillcolor(PIECE)

    pen.pendown()

    pen.begin_fill()

    pen.circle(
        outer_radius,
        steps=96
    )

    pen.end_fill()

    pen.penup()

    # --------------------------------------------------------
    # Inner carved circle
    # --------------------------------------------------------

    pen.setheading(0)

    pen.goto(x, y - inner_radius)

    pen.pencolor(PIECE_DARK)
    pen.pensize(4)

    pen.pendown()

    pen.circle(
        inner_radius,
        steps=96
    )

    pen.penup()

    # --------------------------------------------------------
    # Small highlight
    # --------------------------------------------------------

    highlight_radius = 0.20

    pen.setheading(0)

    pen.goto(
        x - 0.22,
        y + 0.30
    )

    pen.pencolor("#D9D3C4")
    pen.pensize(3)

    pen.pendown()

    pen.circle(
        highlight_radius,
        steps=48
    )

    pen.penup()


# ============================================================
#                     DRAW ONE PIECE
# ============================================================

def draw_piece(row, col, player):
    """
    Draw X or O in a specific board cell.
    """

    if player == 0:
        return

    x, y = cell_center(row, col)

    if player == 1:
        draw_stone_x(x, y)

    elif player == 2:
        draw_stone_o(x, y)


# ============================================================
#                  DRAW WINNING HIGHLIGHT
# ============================================================

def draw_winning_line():
    """
    Draw a golden line through the three
    winning cells.
    """

    if not winning_cells:
        return

    first = winning_cells[0]
    last = winning_cells[-1]

    x1, y1 = cell_center(
        first[0],
        first[1]
    )

    x2, y2 = cell_center(
        last[0],
        last[1]
    )

    win_pen.clear()

    # Outer glow.
    win_pen.pensize(15)
    win_pen.pencolor("#81764B")

    win_pen.penup()
    win_pen.goto(x1, y1)
    win_pen.setheading(
        win_pen.towards(x2, y2)
    )

    win_pen.pendown()
    win_pen.goto(x2, y2)

    # Inner bright line.
    win_pen.pensize(7)
    win_pen.pencolor(WIN_COLOR)

    win_pen.penup()
    win_pen.goto(x1, y1)

    win_pen.pendown()
    win_pen.goto(x2, y2)

    win_pen.penup()


# ============================================================
#                       DRAW EVERYTHING
# ============================================================

def draw_all():
    """
    Completely redraw the game.

    The board variable is the source of truth.

    Graphics are simply a visual representation
    of that data.
    """

    pen.clear()

    # Board background.
    draw_stone_slab()

    # Grid.
    draw_board()

    # Pieces.
    for row in range(3):

        for col in range(3):

            draw_piece(
                row,
                col,
                board[row][col]
            )

    # Winning line.
    if winning_cells:
        draw_winning_line()
    else:
        win_pen.clear()

    screen.update()


# ============================================================
#                       DRAW TEXT
# ============================================================

def draw_header():
    """
    Draw the game title and current status.
    """

    writer.clear()

    # --------------------------------------------------------
    # Game title
    # --------------------------------------------------------

    writer.goto(0, 4.25)

    writer.color(TEXT)

    writer.write(
        "STONE TIC TAC TOE",
        align="center",
        font=("Arial", 24, "bold")
    )

    # --------------------------------------------------------
    # Current message
    # --------------------------------------------------------

    writer.goto(0, 3.78)

    writer.color(TEXT_SECONDARY)

    writer.write(
        current_message,
        align="center",
        font=("Arial", 14, "bold")
    )

    # --------------------------------------------------------
    # Move counter
    # --------------------------------------------------------

    writer.goto(0, -4.15)

    writer.color(TEXT_SECONDARY)

    writer.write(
        f"Moves: {move_count}     •     Press R to restart",
        align="center",
        font=("Arial", 12, "normal")
    )


# ============================================================
#                       BOARD FULL?
# ============================================================

def board_is_full():
    """
    Return True if every cell is occupied.
    """

    for row in range(3):

        for col in range(3):

            if board[row][col] == 0:
                return False

    return True


# ============================================================
#                     WINNING COMBINATIONS
# ============================================================

WINNING_LINES = [

    # Horizontal
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    # Vertical
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    # Diagonal
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


# ============================================================
#                     CHECK FOR WIN
# ============================================================

def get_winner():
    """
    Check all eight possible winning combinations.

    Returns:

        0 = nobody won
        1 = X won
        2 = O won

    Also stores the winning cells.
    """

    global winning_cells

    winning_cells = []

    for line in WINNING_LINES:

        a = line[0]
        b = line[1]
        c = line[2]

        first = board[a[0]][a[1]]
        second = board[b[0]][b[1]]
        third = board[c[0]][c[1]]

        # All three cells must be:
        #
        # 1. non-empty
        # 2. identical

        if (
            first != 0
            and first == second
            and second == third
        ):

            winning_cells = line

            return first

    return 0


# ============================================================
#                     GAME STATUS
# ============================================================

def get_game_result():
    """
    Determine the current game result.

    Returns:

        0 = continue
        1 = X wins
        2 = O wins
        3 = tie
    """

    winner = get_winner()

    # A player won.
    if winner == 1:
        return 1

    if winner == 2:
        return 2

    # Nobody won, so check for tie.
    if board_is_full():
        return 3

    # Game continues.
    return 0


# ============================================================
#                   CHANGE PLAYER
# ============================================================

def switch_turn():
    """
    Change X to O or O to X.
    """

    global turn

    if turn == "X":
        turn = "O"
    else:
        turn = "X"


# ============================================================
#                     PLACE A MARK
# ============================================================

def place_mark(row, col):
    """
    Main game-logic function.

    Steps:

        1. Check if game is over.
        2. Validate coordinates.
        3. Check if cell is empty.
        4. Place X or O.
        5. Increase move counter.
        6. Check for winner.
        7. Check for tie.
        8. Switch player.
        9. Redraw.
    """

    global game_over
    global move_count
    global current_message

    # --------------------------------------------------------
    # 1. Game already finished?
    # --------------------------------------------------------

    if game_over:
        return

    # --------------------------------------------------------
    # 2. Validate row and column.
    # --------------------------------------------------------

    if row < 0 or row > 2:
        return

    if col < 0 or col > 2:
        return

    # --------------------------------------------------------
    # 3. Is the cell already occupied?
    # --------------------------------------------------------

    if board[row][col] != 0:

        current_message = (
            f"Cell is occupied — {turn}'s turn"
        )

        draw_header()
        screen.update()

        return

    # --------------------------------------------------------
    # 4. Place the current player's piece.
    # --------------------------------------------------------

    if turn == "X":
        board[row][col] = 1
    else:
        board[row][col] = 2

    # --------------------------------------------------------
    # 5. Count the successful move.
    # --------------------------------------------------------

    move_count += 1

    # --------------------------------------------------------
    # 6-7. Check game result.
    # --------------------------------------------------------

    result = get_game_result()

    # --------------------------------------------------------
    # X WON
    # --------------------------------------------------------

    if result == 1:

        game_over = True

        current_message = (
            "X WINS!     Press R to play again."
        )

        draw_all()
        draw_header()
        screen.update()

        return

    # --------------------------------------------------------
    # O WON
    # --------------------------------------------------------

    if result == 2:

        game_over = True

        current_message = (
            "O WINS!     Press R to play again."
        )

        draw_all()
        draw_header()
        screen.update()

        return

    # --------------------------------------------------------
    # TIE
    # --------------------------------------------------------

    if result == 3:

        game_over = True

        current_message = (
            "TIE GAME!     Press R to play again."
        )

        draw_all()
        draw_header()
        screen.update()

        return

    # --------------------------------------------------------
    # 8. Change player.
    # --------------------------------------------------------

    switch_turn()

    current_message = f"{turn}'s turn"

    # --------------------------------------------------------
    # 9. Redraw.
    # --------------------------------------------------------

    draw_all()
    draw_header()

    screen.update()


# ============================================================
#                    KEYBOARD INPUT
# ============================================================

def play_key(number):
    """
    Process keyboard input from 1 to 9.
    """

    # Safety check.
    if number < 1 or number > 9:
        return

    row, col = number_to_cell(number)

    place_mark(row, col)


# ============================================================
#                      MOUSE INPUT
# ============================================================

def play_click(x, y):
    """
    Convert the mouse coordinate into
    the correct Tic Tac Toe cell.

    The playable area is exactly:

        x: -3 to +3
        y: -3 to +3
    """

    # --------------------------------------------------------
    # Ignore clicks outside the board.
    # --------------------------------------------------------

    if x < BOARD_LEFT:
        return

    if x > BOARD_RIGHT:
        return

    if y < BOARD_BOTTOM:
        return

    if y > BOARD_TOP:
        return

    # --------------------------------------------------------
    # Determine column.
    #
    # x ranges:
    #
    # -3 to -1 = column 0
    # -1 to +1 = column 1
    # +1 to +3 = column 2
    # --------------------------------------------------------

    col = int((x + 3) / 2)

    # --------------------------------------------------------
    # Determine row.
    #
    # y ranges:
    #
    # +1 to +3 = row 0
    # -1 to +1 = row 1
    # -3 to -1 = row 2
    # --------------------------------------------------------

    row = int((3 - y) / 2)

    # Safety protection.
    if row < 0 or row > 2:
        return

    if col < 0 or col > 2:
        return

    place_mark(row, col)


# ============================================================
#                     RESET GAME
# ============================================================

def reset_game():
    """
    Completely reset the game.
    """

    global board
    global turn
    global game_over
    global move_count
    global current_message
    global winning_cells

    # Empty board.
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # X starts.
    turn = "X"

    # Game becomes active.
    game_over = False

    # Reset move counter.
    move_count = 0

    # Remove winning line.
    winning_cells = []

    # Reset message.
    current_message = "X's turn"

    # Redraw.
    draw_all()
    draw_header()

    screen.update()


# ============================================================
#                     KEYBOARD SETUP
# ============================================================

def setup_keys():
    """
    Connect keys 1-9 and R/r to their functions.
    """

    screen.listen()

    # --------------------------------------------------------
    # Keys 1 through 9
    # --------------------------------------------------------

    for number in range(1, 10):

        key = str(number)

        # Default argument n=number captures the
        # current loop value correctly.
        screen.onkey(
            lambda n=number: play_key(n),
            key
        )

    # --------------------------------------------------------
    # Restart
    # --------------------------------------------------------

    screen.onkey(
        reset_game,
        "r"
    )

    screen.onkey(
        reset_game,
        "R"
    )


# ============================================================
#                       START GAME
# ============================================================

draw_all()

draw_header()

setup_keys()

# Enable mouse input.
screen.onclick(play_click)

# Initial screen update.
screen.update()

# Keep the program alive.
turtle.mainloop()
