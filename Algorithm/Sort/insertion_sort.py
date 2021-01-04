arr = [2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]

# 삽입 정렬
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
print(arr)

# 삽입 정렬 개선
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j - 1] < arr[j]:
            break
        else:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
print(arr)

# 삽입 정렬 개선 2
for idx in range(1, len(arr)):
    i = idx
    to_insert = arr[idx]
    while i > 0 and arr[i - 1] > to_insert:
        arr[i] = arr[i - 1]
        i -= 1
    arr[i] = to_insert
print(arr)
