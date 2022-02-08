import itertools


class KnightGame:

    def __init__(self, columns, rows):
        self.board = {}
        self.columns = columns
        self.rows = rows
        self.column_spaces = len(str(columns))
        self.row_spaces = len(str(rows))
        self.cell_size = len(str(self.columns * self.rows))
        self.border = ' ' * self.row_spaces + '-' * (self.columns * (self.cell_size + 1) + 3)
        self.position = ''
        self.knight = ' ' * (self.cell_size - 1) + 'X'
        self.move = ' ' * (self.cell_size - 1) + 'O'
        self.moves = list(itertools.product(['+1', '-1'], ['+2', '-2'])) + \
                     list(itertools.product(['+2', '-2'], ['+1', '-1']))

    def create_board(self):
        for x in range(1, self.columns + 1):
            for y in range(1, self.rows + 1):
                self.board[f'{x}-{y}'] = '_' * self.cell_size
        return self.board

    def print_board(self):
        print(self.border)
        for y in reversed(range(1, self.rows + 1)):
            row_values = []
            row_number = str(y)
            if len(row_number) < self.row_spaces:
                row_number = ' ' * (self.row_spaces - len(row_number)) + row_number
            for x in range(1, self.columns + 1):
                row_values.append(self.board[f'{x}-{y}'])
            # print(row_number, '|', ' '.join(row_values), '|')
            print(f'{row_number}|', ' '.join(row_values), '|')
        columns_list = []
        for n in range(1, self.columns + 1):
            column_number = str(n)
            if len(column_number) < self.cell_size:
                column_number = ' ' * (self.cell_size - len(column_number)) + column_number
            columns_list.append(column_number)
        print(self.border)
        print(' ' * (self.row_spaces + 1), ' '.join(columns_list))

    def check_move(self, coordinates):
        try:
            x, y = coordinates.split()
            x = int(x)
            y = int(y)
            assert x in range(1, self.columns + 1) and y in range(1, self.rows + 1)
        except (ValueError, AssertionError):
            return False
        else:
            return True

    def get_start(self):
        while True:
            user_input = input("Enter the knight's starting position: ")
            if self.check_move(user_input):
                x, y = user_input.split()
                self.position = '-'.join([str(x), str(y)])
                self.board[self.position] = self.knight
                break
            else:
                print('Invalid dimensions!')

    def get_moves(self):
        moves_list = []
        knight_x, knight_y = self.position.split('-')
        for move in self.moves:
            possible_x = int(knight_x) + int(move[0])
            possible_y = int(knight_y) + int(move[1])
            possible_move = f'{possible_x} {possible_y}'
            if self.check_move(possible_move):
                moves_list.append(f'{possible_x}-{possible_y}')
        for move in moves_list:
            self.board[move] = self.move


def get_dimensions():
    while True:
        dimensions = input('Enter your board dimensions: ')
        try:
            x, y = dimensions.split()
            x = int(x)
            y = int(y)
            assert x > 0 and y > 0
        except (ValueError, AssertionError):
            print('Invalid dimensions!')
        else:
            return dimensions.split()


user_x, user_y = get_dimensions()

game = KnightGame(int(user_x), int(user_y))
game.create_board()
game.get_start()
game.get_moves()
game.print_board()
