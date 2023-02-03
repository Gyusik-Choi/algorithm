def binary_search(start, end, item):
    global ans
    if start > end:
        return

    mid = (start + end) // 2
    if arr[mid] == item:
        ans = True
        return
    elif arr[mid] < item:
        binary_search(mid + 1, end, item)
    else:
        binary_search(start, mid - 1, item)


arr = [1, 3, 5, 7, 9, 11, 13]
ans = False
binary_search(0, len(arr) - 1, 3)
print(ans)
