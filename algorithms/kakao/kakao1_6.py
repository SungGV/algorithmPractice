class board():

    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        # self.board = list(map(lambda x: list(x), board))   # 2D list
        self.board = list(''.join(board))     # 1D list
        self.match_list = []

    def match(self):
        for i in range(self.col * self.col - self.col - 1):
            if i not in range(self.col - 1, self.col * self.row, self.col):  # boundary
                if self.board[i] == self.board[i + 1] and self.board[i] == self.board[i + self.col] and self.board[i] == self.board[i + self.col + 1]:
                    # print(i, i + 1, i + self.col, i + self.col + 1)
                    self.match_list.extend([i, i + 1, i + self.col, i + self.col + 1])

        self.match_list = set(self.match_list)
        self.match_list = list(self.match_list)
        self.match_list.sort(reverse=True)

    def pop(self):
        self.match_list = list(self.match_list)
        for i in self.match_list:

            drop = i
            pop_cnt = 0
            while drop in self.match_list and drop >= 0:
                drop -= self.col
                pop_cnt += 1

            p = pop_cnt
            if drop >= 0:
                for index, j in enumerate(list(range(drop, 0, -self.col))):   # drop list
                    self.board[j], self.board[j + self.col * pop_cnt] = 'X', self.board[j]
                    p -= 1

            else:
                self.board[i] = 'X'

            for m in list(range(i - self.col, i - self.col * (p) - 1, -self.col)):
                self.board[m] = 'X'

            c = i
            for k in list(range(pop_cnt - 1)):
                c -= self.col
                # print(i, c)
                self.match_list.remove(c)


# ["TTTANT",      0  1  2  3  4  5
#  "RRFACC",      6  7  8  9 10 11
#  "RRRFCC",     12 13 14 15 16 17
#  "TRRRAA",     18 19 20 21 22 23
#  "TTMMMF",     24 25 26 27 28 29
#  "TMMTTJ"]     30 31 32 33 34 35

b = board(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])

b.match()
b.pop()

for i, v in enumerate(b.board):
    print(v, end=' ')
    if (i + 1) % 6 == 0:
        print("")


