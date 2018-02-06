l = [38,27,43,3,9,82,10]

def merge(data, start, mid, end):
    # i = start
    # j = mid + 1
    #
    # new_data = []
    #
    # while i <= mid and j <= end:
    #     if data[i] < data[j]:
    #         new_data.append(data[i])
    #         i += 1
    #     else:
    #         new_data.append(data[j])
    #         j += 1
    #
    # if i > mid:
    #     new_data += data[j:end+1]
    # else:
    #     new_data += data[i:mid + 1]
    #
    # t = 0
    # for i in new_data:
    #     data[start + t] = i
    #     t += 1

    left = [data[i] for i in range(start, mid+1)]
    right = [data[i] for i in range(mid+1, end+1)]

    i = 0
    j = 0
    k = start
    while i <= len(left)-1 and j <= len(right)-1:
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i <= len(left)-1:
        data[k] = left[i]
        k += 1
        i += 1
    while j <= len(right)-1:
        data[k] = right[j]
        k += 1
        j += 1


def merge_sort(data, start, end, fr):

    if end > start:

        mid = int((start + end ) / 2)
        print(start, mid, end, fr)
        merge_sort(data, start, mid, 'l')
        merge_sort(data, mid+1, end, 'r')

        merge(data, start, mid, end)

print(l)
merge_sort(l, 0, len(l)-1, 'first')
print(l)




# merge sort with iteration


