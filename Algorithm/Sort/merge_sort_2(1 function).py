def merge_sort(low, high):
    if high - low < 2:
        return
    mid = (high + low) // 2
    merge_sort(low, mid)
    merge_sort(mid, high)
    temp = []
    l, h = low, mid

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < high:
        temp.append(arr[h])
        h += 1
    for i in range(low, high):
        arr[i] = temp[i - low]


arr = [2, 1, 5, 3, 4]
merge_sort(0, len(arr))
print(arr)
