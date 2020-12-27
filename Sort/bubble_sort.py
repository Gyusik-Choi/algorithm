arr = [2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]

# 버블 정렬
arr_b = copy.deepcopy(arr)
for i in range(len(arr_b) - 1):
    for j in range(i+1, len(arr_b)):
        if arr_b[i] > arr_b[j]:
            arr_b[i], arr_b[j] = arr_b[j], arr_b[i]
print(arr_b)
