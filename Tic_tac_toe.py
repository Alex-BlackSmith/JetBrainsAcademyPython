class TicTacField():
    lv_border = '| '
    rv_border = ' |\n'
    h_border = '---------\n'
    win_combinations = ['012', '345', '678', '036', '147', '258', '048', '246']
    initial_inp = False
    x_turn = True
    o_turn = False
    def __init__(self):
        self.game_field_list = 9 * ['_']

    def create_view(self):
        result_string = ''
        for i in range(0, 9, 3):
            result_string += TicTacField.lv_border + ' '.join(self.game_field_list[i:i+3]) + TicTacField.rv_border
        return TicTacField.h_border + result_string + TicTacField.h_border

    def show(self, status=5):
        status_dict = {4: "Impossible",
                       3: "Game not finished",
                       2: "Draw",
                       1: "X wins",
                       0: "O wins"}
        print(self.create_view())
        if 0 <= status <= 2:
            print(status_dict[status])


    def read_input(self, inp=None):
        successfull_read = True
        if inp == None and not TicTacField.initial_inp:
            self.game_field_list = list(input("Enter cells: "))
            TicTacField.initial_inp = True
        elif TicTacField.initial_inp:
            try:
                x, y = map(int, input("Enter the coordinates: ").split())
                if x < 1 or x > 3 or y < 1 or y > 3:
                    print('Coordinates should be from 1 to 3!')
                    successfull_read = False
                elif self.game_field_list[(x - 1) + (3 - y) * 3] == 'X' \
                   or self.game_field_list[(x - 1) + (3 - y) * 3] == 'O':
                    print('This cell is occupied! Choose another one!')
                    successfull_read = False
                else:
                    copy_game_field = list(self.game_field_list)
                    copy_game_field[(x - 1) + (3 - y) * 3] = 'X' if TicTacField.x_turn else 'O'
                    self.game_field_list = ''.join(copy_game_field)
                    TicTacField.x_turn, TicTacField.o_turn = TicTacField.o_turn, TicTacField.x_turn
            except ValueError:
                print('You should enter numbers!')
                successfull_read = False
        else:
            TicTacField.initial_inp = True
            self.game_field_list = inp
        return successfull_read

    def get_status(self):
        indexes_O = ''
        indexes_X = ''
        wins_O = False
        wins_X = False
        for i in range(0,9):
            if self.game_field_list[i] =='O':
                indexes_O += ''.join(str(i))
            if self.game_field_list[i] =='X':
                indexes_X += ''.join(str(i))
        for comb in TicTacField.win_combinations:
            if comb[0] in indexes_O and comb[1] in indexes_O and comb[2] in indexes_O:
                wins_O = True
            if comb[0] in indexes_X and comb[1] in indexes_X and comb[2] in indexes_X:
                wins_X = True
        if wins_O and wins_X or self.game_field_list.count('X') - self.game_field_list.count('O') >= 2:
            return 4
        elif not (wins_O or wins_X) and self.game_field_list.count('_') > 0:
            return 3
        elif not (wins_O or wins_X) and self.game_field_list.count('_') == 0:
            return 2
        elif wins_X:
            return 1
        elif wins_O:
            return 0


session = TicTacField()
session.read_input()
session.show()
read_counter = 0
while True:
    if session.read_input():
        game_continue = session.get_status()
        session.show(game_continue)
        if game_continue <= 2:
            break
    else:
        continue
