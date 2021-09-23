
# Create a new board

def create_new_board(num_rows, num_columns):
    board = []
    for row in range(num_rows):
        board.append([])
        for column in range(num_columns):
            board[row].append(0)
    return board

# Print board
num_rows = 5
num_columns = 6
board = create_new_board(num_rows, num_columns)
print(board)


def set_cell(row, column, value):
    board[row][column] = value

set_cell(2,2, 1)

# count the number of living neighbors
def count_living_neighbors(row, column):
    count = 0
    for row in range(row - 1, row + 1):
        if (row >= 0) and (row <= num_rows):
            for column in range(column - 1, column + 1):
                if (column >= 0) and (column <= num_columns):
                    count = count + board[row][column]
    if board[row][column] == 1:
        count = count - 1
    return count

print(board)

print (count_living_neighbors(2,2))

def get_next_gen_cell(board, row, column):
    next_gen_cell = 0
    num_live_neighbors = count_living_neighbors(row, column)
    if (board[row][column] == 1):
        if ((num_live_neighbors < 2) or (num_live_neighbors > 3)):
            next_gen_cell = 0
        else:
            next_gen_cell = 1
    elif (num_live_neighbors == 3):
        next_gen_cell = 1
    return next_gen_cell

def generate_next_board(board):
    new_board = create_new_board(num_rows, num_columns)
    for row in range(num_rows):
        for column in range(num_columns):
            new_board[row][column] = get_next_gen_cell(board, row, column)
    return new_board

board1 = generate_next_board(board)

print(board1)
