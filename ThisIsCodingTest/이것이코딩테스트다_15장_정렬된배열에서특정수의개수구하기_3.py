def binary_search_right(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    # if numbers[mid] == target and numbers[mid + 1] > target:
    # 위의 조건문은 index error 가 발생할 수 있다
    if numbers[mid] == target and (mid == N - 1 or numbers[mid + 1] > target):
        return mid
    else:
        if numbers[mid] > target:
            return binary_search_right(start, mid - 1, target)
        return binary_search_right(mid + 1, end, target)


def binary_search_left(start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    # if numbers[mid] == target and numbers[mid - 1] < target:
    # binary_search_right 와는 다르게 위의 조건문으로 해도 index error 는 발생하지 않는다
    # 파이썬의 문법 특성상 음수 인덱스도 존재하기 때문이다
    if numbers[mid] == target and (mid == 0 or numbers[mid - 1] < target):
        return mid
    else:
        # 이 부분에서 주의(> 가 아니라 >= 로 했다)
        # 위의 if 문에서 numbers[mid] 가 2 일지라도 그 다음의 and 조건을 충족하지 못했을 수 있다
        if numbers[mid] >= target:
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
