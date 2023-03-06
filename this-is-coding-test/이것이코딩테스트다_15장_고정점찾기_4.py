def binary_search(low, high):
    while low < high:
        mid = (low + high) // 2

        if numbers[mid] >= mid:
            high = mid
        else:
            low = mid + 1

    return low


N = int(input())
numbers = list(map(int, input().split()))

idx = binary_search(0, len(numbers) - 1)

# 리턴한 값이 고정점 아니면 -1 출력
if numbers[idx] != idx:
    print(-1)
else:
    print(idx)

# 5
# -15 -6 1 3 7
