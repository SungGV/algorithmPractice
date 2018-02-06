n = 8
col = [0 for _ in range(n+1)]

def position_check(level):
    for i in range(1, level):
        if col[i] == col[level]:
            return False
        elif level - i == abs(col[i]-col[level]):
            return False
    return True

c = 0
def n_queen(level):

    if not position_check(level):
        return False
    elif level == n:
        for i in range(1, n+1):
            print(i, col[i],  end=' ')
        global c
        c += 1
        print(c)
    else:
        for i in range(1, n+1):
            col[level+1] = i
            if n_queen(level+1):
                return True
        return False
    return False

n_queen(0)