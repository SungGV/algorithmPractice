import random

random.seed(123)
board = [[random.randint(1,50) for _ in range(5)] for _ in range(5)]

# recursion
def find_path(i, j):
    if i == 0 and j == 0:
        return board[i][j]
    elif i == 0:
        return find_path(i, j-1) + board[i][j]
    elif j == 0:
        return find_path(i-1, j) + board[i][j]
    else:
        return min(find_path(i-1, j), find_path(i, j-1)) + board[i][j]


print(find_path(4, 4))


# top-down
store_score = [[-1 for _ in range(5)] for _ in range(5)]
def find_path_top_down(i, j):
    if store_score[i][j] > 0:
        return store_score[i][j]
    if i == 0 and j == 0:
        store_score[i][j] = board[i][j]
    elif i == 0:
        store_score[i][j] = find_path_top_down(i, j-1) + board[i][j]
    elif j == 0:
        store_score[i][j] = find_path_top_down(i-1, j) + board[i][j]
    else:
        store_score[i][j] = min(find_path_top_down(i-1, j), find_path_top_down(i, j-1)) + board[i][j]
    return store_score[i][j]

print(find_path_top_down(4, 4))


# bottom-up
store_score2 = [[-1 for _ in range(5)] for _ in range(5)]
def find_path_bottom_up(i, j):
    for r in range(i+1):
        for c in range(j+1):
            if r == 0 and c == 0:
                store_score2[r][c] = board[r][c]
            elif r == 0:
                store_score2[r][c] = store_score2[r][c-1] + board[r][c]
            elif c == 0:
                store_score2[r][c] = store_score2[r-1][c] + board[r][c]
            else:
                store_score2[r][c] = min(store_score2[r-1][c], store_score2[r][c-1]) + board[r][c]
    return store_score2[r][c]

print(find_path_bottom_up(4,4))