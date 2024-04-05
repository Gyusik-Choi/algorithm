def binary_search(arr, num):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] == num:
            return mid

        if arr[mid] > num:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("can't find num in arr")


# 참고
# 파이썬 알고리즘 인터뷰
