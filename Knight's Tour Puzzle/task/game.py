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

    def get_start(self):
        while True:
            user_input = input("Enter the knight's starting position: ")
            try:
                x, y = user_input.split()
                x = int(x)
                y = int(y)
                assert x in range(1, self.columns + 1) and y in range(1, self.rows + 1)
            except (ValueError, AssertionError):
                print('Invalid dimensions!')
            else:
                self.board['-'.join([str(x), str(y)])] = self.knight
                break


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
game.print_board()
