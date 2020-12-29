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
