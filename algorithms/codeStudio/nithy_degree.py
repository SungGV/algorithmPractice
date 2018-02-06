def get_ninty_degree(h, m):

    h_degree = h * 30 + (m * .5)
    m_degree = (m * 6)

    if h_degree > 360:
        h_degree -= 360

    # print(h, m, h_degree, m_degree, 'before')

    degree = abs(h_degree - m_degree)
    if 180 < degree:
        if h_degree > m_degree:
            degree = 360-h_degree + m_degree
        else:
            degree = 360 - m_degree + h_degree

    # print(degree, 'final')

    if 87 <= degree <= 92:
        return True
    return False


cnt = 0
for h in range(0, 24):
    for m in range(60):
        if get_ninty_degree(h, m):
            cnt +=1
            print(h, 'hour', m, 'minute')

print('total', cnt)



#
# for n in range(1, 45):
#     h=(6*n-3)/11.0
#     m = (h-int(h))*60
#     print ("%02d:%02d"%(h,m))
# print ("Total:44번!")