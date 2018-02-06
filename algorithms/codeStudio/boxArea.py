c_box = [[1,4,3,4], [2,3,4,1], [3,4,2,1], [9,3,2,1]]
r_box = list(zip(*c_box))

def get_area(box):
    area = 0
    for r in range(len(box)):
        prev = box[r][0]
        area += prev
        area += 1
        for c in range(1, len(box[r])):
            area += abs(prev - box[r][c])
            prev = box[r][c]
            if box[r][c] > 0:
                area += 1
        area += prev
    return area


print(get_area(c_box) + get_area(r_box))
print()

