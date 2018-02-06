
lst_len, window_len = 8, 3
lst = [1, 3, -1, -3, 5, 3, 6, 7]

min_list = []
max_list = []

first_window = lst[:window_len]
temp_max = max(first_window)
temp_min = min(first_window)

max_list.append(temp_max)
min_list.append(temp_min)

for i in lst[window_len:]:
    if i > temp_max:
        temp_max = i

    elif i < temp_min:
        print(temp_min, i)
        temp_min = i

    max_list.append(temp_max)
    min_list.append(temp_min)

print('Min', min_list)
print('Max', max_list)



