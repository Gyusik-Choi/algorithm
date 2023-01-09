def binary_search_right(start, end, target):
    if start >= end:
        if numbers[end] == target:
            return end

        return -1

    mid = (start + end) // 2

    if numbers[mid] == target:
        if (mid < N - 1 and numbers[mid + 1] > target) or mid == N - 1:
            return mid
        else:
            return binary_search_right(mid + 1, end, target)
    else:
        if numbers[mid] > target:
            return binary_search_right(start, mid - 1, target)

        return binary_search_right(mid + 1, end, target)


def binary_search_left(start, end, target):
    if start >= end:
        if numbers[end] == target:
            return end

        return -1

    mid = (start + end) // 2

    if numbers[mid] == target:
        if (mid > 0 and numbers[mid - 1] < target) or mid == 0:
            return mid
        else:
            return binary_search_left(start, mid - 1, target)
    else:
        if numbers[mid] > target:
            return binary_search_left(start, mid - 1, target)

        return binary_search_left(mid + 1, end, target)


N, x = map(int, input().split())
numbers = list(map(int, input().split()))

left_idx = binary_search_left(0, N - 1, x)
right_idx = binary_search_right(0, N - 1, x)

if left_idx == -1 or right_idx == -1:
    print(-1)
else:
    print(right_idx - left_idx + 1)

# 7 2
# 1 1 2 2 2 2 3

# 참고
# https://velog.io/@xxwb__/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
