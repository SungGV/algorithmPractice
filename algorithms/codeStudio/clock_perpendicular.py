
def get_ninth_degree(h, m):

    h_degree = h * 30 + (m * .5)
    m_degree = (m * 6)
    print(h_degree, m_degree, 'before')

    while h_degree >= 95:
        h_degree -= 90

    while m_degree >= 95:
        m_degree -= 90
    print(h_degree, m_degree, 'after')

    degree = abs(h_degree - m_degree)
    print(degree, 'final')

    if 86.5 <= degree <= 92:
        return True
    return False



# print(get_ninth_degree(9, 16))
cnt = 0
for h in range(6, 8):
    for m in range(60):
        if get_ninth_degree(h, m):
            cnt +=1
            print(h, 'hour', m, 'minute')

print('total', cnt)