def partition(low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low


def quick_sort(low, high):
    if high - low < 2:
        return
    mid = partition(low, high)
    quick_sort(low, mid - 1)
    quick_sort(mid, high)


arr = [5, 1, 4, 3, 2]
quick_sort(0, len(arr) - 1)
print(arr)

# 참고
# https://www.daleseo.com/sort-quick/