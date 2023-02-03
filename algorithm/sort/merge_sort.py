def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    if l == len(low_arr):
        while h < len(high_arr):
            merged_arr.append(high_arr[h])
            h += 1
    elif h == len(high_arr):
        while l < len(low_arr):
            merged_arr.append(low_arr[l])
            l += 1
    return merged_arr


lst = [5, 1, 4, 3, 2]
print(merge_sort(lst))

# 참고
# https://www.daleseo.com/sort-merge/
