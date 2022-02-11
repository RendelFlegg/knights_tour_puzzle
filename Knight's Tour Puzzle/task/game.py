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
        self.position = None
        self.move_list = ' '
        self.knight = ' ' * (self.cell_size - 1) + 'X'
        self.visited = ' ' * (self.cell_size - 1) + '*'
        self.moves = list(itertools.product(['+1', '-1'], ['+2', '-2'])) + \
                     list(itertools.product(['+2', '-2'], ['+1', '-1']))
        self.visited_cells = []

    def create_board(self):
        for x in range(1, self.columns + 1):
            for y in range(1, self.rows + 1):
                self.board[f'{x}-{y}'] = '_' * self.cell_size
        return self.board

    def update_board(self):
        for key in self.board:
            if key == self.position:
                self.board[key] = self.knight
                for move in self.move_list:
                    clear_moves = [n for n in self.get_moves(move) if n not in self.visited_cells]
                    move_counter = ' ' * (self.cell_size - 1) + str(len(clear_moves))
                    self.board[move] = move_counter
            elif key in self.visited_cells:
                self.board[key] = self.visited
            elif key not in self.get_moves(self.position):
                self.board[key] = '_' * self.cell_size

    def print_board(self):
        self.update_board()
        print(self.border)
        for y in reversed(range(1, self.rows + 1)):
            row_values = []
            row_number = str(y)
            if len(row_number) < self.row_spaces:
                row_number = ' ' * (self.row_spaces - len(row_number)) + row_number
            for x in range(1, self.columns + 1):
                row_values.append(self.board[f'{x}-{y}'])
            print(f'{row_number}|', ' '.join(row_values), '|')
        columns_list = []
        for n in range(1, self.columns + 1):
            column_number = str(n)
            if len(column_number) < self.cell_size:
                column_number = ' ' * (self.cell_size - len(column_number)) + column_number
            columns_list.append(column_number)
        print(self.border)
        print(' ' * (self.row_spaces + 1), ' '.join(columns_list))

    def check_move(self, coordinates, player=False):
        try:
            x, y = coordinates.split()
            x = int(x)
            y = int(y)
            assert x in range(1, self.columns + 1) and y in range(1, self.rows + 1)
        except (ValueError, AssertionError):
            if player:
                print('Invalid dimensions!')
            return False
        else:
            if f'{x}-{y}' in self.visited_cells or \
                    player and self.position and f'{x}-{y}' not in self.get_moves(self.position):
                if player:
                    print('Invalid move!', end=' ')
                return False
            return True

    def get_move(self):
        while True:
            if not self.position:
                user_input = input("Enter the knight's starting position: ")
            else:
                user_input = input('Enter your next move: ')
            if self.check_move(user_input, player=True):
                x, y = user_input.split()
                self.position = '-'.join([str(x), str(y)])
                self.move_list = [n for n in self.get_moves(self.position) if n not in self.visited_cells]
                self.board[self.position] = self.knight
                self.visited_cells.append(self.position)
                break

    def get_moves(self, position):
        moves_list = []
        knight_x, knight_y = position.split('-')
        for move in self.moves:
            possible_x = int(knight_x) + int(move[0])
            possible_y = int(knight_y) + int(move[1])
            possible_move = f'{possible_x} {possible_y}'
            if self.check_move(possible_move):
                moves_list.append(f'{possible_x}-{possible_y}')
        return moves_list


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
while game.move_list:
    game.get_move()
    game.print_board()

if len(game.board) == len(game.visited_cells):
    print('What a great tour! Congratulations!')
else:
    print('No more possible moves!')
    print(f'Your knight visited {len(game.visited_cells)} squares!')
