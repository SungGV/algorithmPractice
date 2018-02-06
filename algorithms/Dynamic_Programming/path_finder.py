import random
board = [[random.randint(0,5) for _ in range(5)] for _ in range(5)]


def path_finder(i, j):
    store = [[-1 for _ in range(i)] for _ in range(j)]
    rst = [[-1 for _ in range(i)] for _ in range(j)]
    for row in range(i):
        for col in range(j):
            if row == 0 and col == 0:
                store[row][col] = board[row][col]
            elif row == 0:
                store[row][col] = store[row][col-1] + board[row][col]
                rst[row][col] = '-'
            elif col == 0:
                store[row][col] = store[row-1][col] + board[row][col]
                rst[row][col] = '-'
            else:
                left = store[row-1][col]
                up = store[row][col-1]
                store[row][col] = min(left, up) + board[row][col]
                if left > up:
                    rst[row][col] = 'left'
                else:
                    rst[row][col] = 'up'
    for i in board:
        print(i)
    print()
    for i in store:
        print(i)
    print()
    for i in rst:
        print(i)
    return store[-1][-1]

print(path_finder(4,4))