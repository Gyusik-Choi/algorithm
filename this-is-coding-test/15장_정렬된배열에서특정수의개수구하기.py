def binary_search_right(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if numbers[mid] == target:
        if mid + 1 < N:
            if numbers[mid + 1] > target:
                return mid
            return binary_search_right(mid + 1, end, target)
        else:
            return -1
    else:
        if numbers[mid] > target:
            return binary_search_right(start, mid - 1, target)
        return binary_search_right(mid + 1, end, target)


def binary_search_left(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if numbers[mid] == target:
        if mid - 1 >= 0:
            if numbers[mid - 1] < target:
                return mid
            return binary_search_left(start, mid - 1, target)
        else:
            return -1
    else:
        if numbers[mid] > target:
            return binary_search_left(start, mid - 1, target)
        return binary_search_left(mid + 1, end, target)


N, x = map(int, input().split())
numbers = list(map(int, input().split()))

left_idx = binary_search_left(0, N - 1, x)
right_idx = binary_search_right(0, N - 1, x)

if left_idx == -1 and right_idx == -1:
    print(-1)
else:
    if left_idx == -1:
        print(right_idx + 1)
    elif right_idx == -1:
        print(N - left_idx)
    else:
        print(right_idx - left_idx + 1)
