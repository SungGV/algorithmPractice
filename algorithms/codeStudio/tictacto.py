class Tictactoe:

    def __init__(self, r, c):
        self.board = [i for i in range(1, r*c + 1)]
        self.available_position = []
        self.available_position.extend(self.board)
        self.current_player = True  # player1

    def display(self):
        for i in range(len(self.board)):
            print(self.board[i], end= ' ')
            if (i+1) % 3 == 0:
                print()

    def is_win(self):
        pass

    def is_position_available(self, index):
        if self.board[index] != "X" and self.board[index] != "Y":
            return True
        return False

    def place(self, index, sym):
        index -= 1
        if self.is_position_available(index):
            self.board[index] = sym
            del self.available_position[index]
            self.current_player = not self.current_player

        else:
            print('not an available position')

    def show_available_position(self):
        print(' '.join(map(lambda x: str(x), self.available_position)))

game = Tictactoe(3,3)
game.display()
game.place(5,'X')
game.display()
game.place(5,'X')
game.display()
game.show_available_position()