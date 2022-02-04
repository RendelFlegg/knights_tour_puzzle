def create_board():
    dictionary = {}
    for x in range(1, 9):
        for y in range(1, 9):
            dictionary[f'{x}-{y}'] = '_'
    return dictionary


def print_board(dictionary):
    print(' ', '-------------------')
    for y in reversed(range(1, 9)):
        row_values = []
        for x in range(1, 9):
            row_values.append(dictionary[f'{x}-{y}'])
        print(y, '|', ' '.join(row_values), '|')
    print(' ', '-' * 19)
    print(' ' * 3, ' '.join([str(n) for n in range(1, 9)]))


def get_start():
    while True:
        user_input = input("Enter the knight's starting position: ")
        try:
            x, y = user_input.split()
            x = int(x)
            y = int(y)
            assert x in range(1, 9) and y in range(1, 9)
        except (ValueError, AssertionError):
            print('Invalid dimensions!')
        else:
            return '-'.join([str(x), str(y)])


board = create_board()
start = get_start()
board[start] = 'X'
print_board(board)
