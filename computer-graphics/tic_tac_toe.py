import turtle

# Colors
BG = "#5C5C52"
SLAB = "#8E8E7E"
GROOVE = "#3D3D36"
PIECE = "#B5AE9E"
PIECE_DARK = "#6B655A"
TEXT = "#E8E4D9"
WIN = "#D6C27A"


# Screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Stone Tic Tac Toe")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor(BG)
screen.tracer(0, 0)

pen = turtle.Turtle(visible=False)
writer = turtle.Turtle(visible=False)
win_pen = turtle.Turtle(visible=False)

writer.penup()


# Game data
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

turn = "X"
game_over = False
moves = 0
winning_line = []


# --------------------------------------------------
# Board positions
# --------------------------------------------------

def cell_xy(row, col):
    """Get the center of a cell."""
    x = -2 + (col * 2)
    y = 2 - (row * 2)
    return x, y


def number_to_cell(number):
    """Change 1-9 into row and column."""
    number -= 1
    return number // 3, number % 3


# --------------------------------------------------
# Drawing the board
# --------------------------------------------------

def draw_slab():
    """Draw the stone background."""

    pen.penup()
    pen.goto(-3.4, 3.4)
    pen.setheading(0)

    pen.color(PIECE_DARK, SLAB)
    pen.begin_fill()

    for _ in range(4):
        pen.forward(6.8)
        pen.right(90)

    pen.end_fill()


def draw_board():
    """Draw the four grid lines."""

    pen.pensize(8)
    pen.pencolor(GROOVE)

    # Horizontal lines
    for y in (-1, 1):
        pen.penup()
        pen.goto(-3, y)
        pen.setheading(0)
        pen.pendown()
        pen.forward(6)

    # Vertical lines
    for x in (-1, 1):
        pen.penup()
        pen.goto(x, -3)
        pen.setheading(90)
        pen.pendown()
        pen.forward(6)

    pen.penup()


# --------------------------------------------------
# Drawing X and O
# --------------------------------------------------

def draw_x(x, y):
    """Draw an X."""

    size = 0.60

    # Dark part
    pen.pensize(12)
    pen.pencolor(PIECE_DARK)

    pen.penup()
    pen.goto(x - size, y - size)
    pen.setheading(45)
    pen.pendown()
    pen.forward(size * 2 * 1.414)

    pen.penup()
    pen.goto(x - size, y + size)
    pen.setheading(-45)
    pen.pendown()
    pen.forward(size * 2 * 1.414)

    # Light part
    size = 0.52
    pen.pensize(7)
    pen.pencolor(PIECE)

    pen.penup()
    pen.goto(x - size, y - size)
    pen.setheading(45)
    pen.pendown()
    pen.forward(size * 2 * 1.414)

    pen.penup()
    pen.goto(x - size, y + size)
    pen.setheading(-45)
    pen.pendown()
    pen.forward(size * 2 * 1.414)

    pen.penup()


def draw_o(x, y):
    """Draw an O."""

    radius = 0.68

    pen.penup()

    # Reset heading so the circle is always centered.
    pen.setheading(0)
    pen.goto(x, y - radius)

    pen.pensize(4)
    pen.pencolor(PIECE_DARK)
    pen.fillcolor(PIECE)

    pen.pendown()
    pen.begin_fill()
    pen.circle(radius, steps=80)
    pen.end_fill()

    # Inner ring
    pen.penup()
    pen.setheading(0)
    pen.goto(x, y - 0.42)

    pen.pensize(3)
    pen.pencolor(PIECE_DARK)

    pen.pendown()
    pen.circle(0.42, steps=80)

    pen.penup()


def draw_piece(row, col, player):
    """Draw the piece in a cell."""

    if player == 0:
        return

    x, y = cell_xy(row, col)

    if player == 1:
        draw_x(x, y)
    else:
        draw_o(x, y)


# --------------------------------------------------
# Winning line
# --------------------------------------------------

def draw_winning_line():
    """Draw a line over the winning pieces."""

    if not winning_line:
        return

    first = winning_line[0]
    last = winning_line[-1]

    x1, y1 = cell_xy(first[0], first[1])
    x2, y2 = cell_xy(last[0], last[1])

    win_pen.clear()
    win_pen.pensize(10)
    win_pen.pencolor(WIN)

    win_pen.penup()
    win_pen.goto(x1, y1)
    win_pen.setheading(win_pen.towards(x2, y2))
    win_pen.pendown()
    win_pen.goto(x2, y2)
    win_pen.penup()


# --------------------------------------------------
# Redraw everything
# --------------------------------------------------

def draw_all():
    pen.clear()

    draw_slab()
    draw_board()

    for row in range(3):
        for col in range(3):
            draw_piece(row, col, board[row][col])

    draw_winning_line()

    screen.update()


# --------------------------------------------------
# Text
# --------------------------------------------------

def show_message(message):
    writer.clear()

    writer.goto(0, 4.1)
    writer.color(TEXT)
    writer.write(
        "STONE TIC TAC TOE",
        align="center",
        font=("Arial", 22, "bold")
    )

    writer.goto(0, 3.65)
    writer.write(
        message,
        align="center",
        font=("Arial", 14, "bold")
    )

    writer.goto(0, -4.1)
    writer.write(
        f"Moves: {moves}    |    Press R to restart",
        align="center",
        font=("Arial", 11, "normal")
    )


# --------------------------------------------------
# Game checking
# --------------------------------------------------

winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


def check_winner():
    """Return the winner and winning line."""

    for line in winning_combinations:

        a = line[0]
        b = line[1]
        c = line[2]

        p1 = board[a[0]][a[1]]
        p2 = board[b[0]][b[1]]
        p3 = board[c[0]][c[1]]

        if p1 != 0 and p1 == p2 == p3:
            return p1, line

    return 0, []


def board_full():
    """Check if there are no empty cells."""

    for row in board:
        if 0 in row:
            return False

    return True


# --------------------------------------------------
# Making a move
# --------------------------------------------------

def place_mark(row, col):
    global turn
    global game_over
    global moves
    global winning_line

    if game_over:
        return

    # Don't use a cell twice.
    if board[row][col] != 0:
        show_message(f"Cell already used - {turn}'s turn")
        return

    # Put X or O on the board.
    if turn == "X":
        board[row][col] = 1
    else:
        board[row][col] = 2

    moves += 1

    # Check for a winner.
    winner, line = check_winner()

    if winner == 1:
        winning_line = line
        game_over = True
        draw_all()
        show_message("X wins! Press R to play again.")
        return

    if winner == 2:
        winning_line = line
        game_over = True
        draw_all()
        show_message("O wins! Press R to play again.")
        return

    # Check for a tie.
    if board_full():
        game_over = True
        draw_all()
        show_message("Tie game! Press R to play again.")
        return

    # Change player.
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    draw_all()
    show_message(f"{turn}'s turn")


# --------------------------------------------------
# Keyboard
# --------------------------------------------------

def play_key(number):
    row, col = number_to_cell(number)
    place_mark(row, col)


# --------------------------------------------------
# Mouse
# --------------------------------------------------

def play_click(x, y):
    """Turn a mouse click into a board position."""

    # Ignore clicks outside the board.
    if x < -3 or x > 3 or y < -3 or y > 3:
        return

    col = int((x + 3) // 2)
    row = int((3 - y) // 2)

    if 0 <= row <= 2 and 0 <= col <= 2:
        place_mark(row, col)


# --------------------------------------------------
# Restart
# --------------------------------------------------

def reset_game():
    global board
    global turn
    global game_over
    global moves
    global winning_line

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    turn = "X"
    game_over = False
    moves = 0
    winning_line = []

    win_pen.clear()

    draw_all()
    show_message("X's turn")


# --------------------------------------------------
# Set up controls
# --------------------------------------------------

def setup_keys():
    screen.listen()

    for number in range(1, 10):
        screen.onkey(
            lambda n=number: play_key(n),
            str(number)
        )

    screen.onkey(reset_game, "r")
    screen.onkey(reset_game, "R")


# Start the game
draw_all()
show_message("X's turn")

setup_keys()
screen.onclick(play_click)

turtle.mainloop()
