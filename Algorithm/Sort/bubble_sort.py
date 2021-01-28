# 거품정렬
arr = [5, 2, 1, 3, 4]
N = len(arr) - 1
for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        else:
            break
print(arr)

# 거품정렬 개선
arr = [5, 2, 1, 3, 4]
N = len(arr) - 1
for i in range(N - 1, -1, -1):
    swapped = False
    for j in range(i + 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break
print(arr)

# 거품정렬 추가 개선
arr = [5, 2, 1, 3, 4]
idx = len(arr) - 1
while idx > 0:
    for i in range(idx):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            idx = i
print(arr)

# 참고
# https://www.daleseo.com/sort-bubble/