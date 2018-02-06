class Tictactoe:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.board = [str(i) for i in range(1, r * c + 1)]
        self.current_player = 'X'  # player1
        self.place_count = 0

    def display(self):
        for i in range(len(self.board)):
            print(self.board[i], end=' ')
            if (i + 1) % 3 == 0:
                print()

    def is_win(self):
        # this can be done much easier if use 2D array

        for i in range(0, self.row * self.col, self.col+1): # 대각선 왼쪽위 -> 오른쪽 아래
            if self.board[i] != self.current_player:
                break
        else:
            return True

        for i in range(self.col-1, self.row * self.col-self.col + 1, self.col-1): # 대각선
            if self.board[i] != self.current_player:
                break
        else:
            return True

        for i in range(0, self.row * self.col - self.col + 1, self.col):
            for j in range(i, i+self.col):   #  세로
                if self.board[j] != self.current_player:
                    break
            else:
                return True

        for i in range(0, self.col):
            for j in range(i, i + (self.row-1) * self.col + 1, self.col):
                if self.board[j] != self.current_player: # 가로
                    break
            else:
                return True
        return False

    def is_tie(self):
        if self.place_count == self.col * self.row:
            return True
        return False

    def is_position_available(self, index):
        if self.board[index] != "X" and self.board[index] != "Y":
            return True
        return False

    def place(self, index):
        index -= 1
        if self.is_position_available(index):
            self.board[index] = self.current_player
            self.place_count += 1
        else:
            print('not an available position')

    def switch_player(self):
        if self.current_player == 'O':
            self.current_player = 'X'
        else:
            self.current_player = 'O'

    def show_available_position(self):
        print('Available positions are :', ' '.join(filter(lambda x: x.isdigit(), self.board)))


game = Tictactoe(3, 3)
game.display()
while True:
    place = input('place it(q for quit)')
    if place == 'q':
        break
    game.place(int(place))
    game.display()
    if game.is_win():
        print(game.current_player, 'won the game')
        break
    if game.is_tie():
        print('tie game')
        break

    game.switch_player()
    game.show_available_position()
    print()
print('game terminated')
