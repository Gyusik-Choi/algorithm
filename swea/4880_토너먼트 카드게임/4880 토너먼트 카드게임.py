def split(start, end):
    if start == end:
        return start

    low = split(start, (start + end) // 2)
    high = split((start + end) // 2 + 1, end)

    if (arr[low] == 1 and arr[high] == 2) or (arr[low] == 2 and arr[high] == 3) or (arr[low] == 3 and arr[high] == 1):
        return high
    elif arr[low] == arr[high]:
        return low
    else:
        return low


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = split(0, len(arr) - 1)
    print("#{} {}".format(t, ans + 1))

