# 거품정렬
def bubble_sort(arr):
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 거품정렬 개선
def bubble_sort2(arr):
    for i in range(N - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

# 거품정렬 추가 개선
def bubble_sort3(arr):
    idx = len(arr) - 1

    while idx > 0:
        for i in range(idx):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                idx = i

    return arr

# 참고
# https://www.daleseo.com/sort-bubble/
