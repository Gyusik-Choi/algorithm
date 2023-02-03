def binary_search(start, end, target):
    while start < end:
        mid = (start + end) // 2

        if lis[mid] >= target:
            end = mid
        else:
            start = mid + 1

    return start


N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]
wires.sort(key=lambda x: x[0])

lis = [wires[0][1]]

for i in range(1, N):
    if lis[-1] < wires[i][1]:
        lis.append(wires[i][1])
    else:
        # end 값에 주의
        idx = binary_search(0, len(lis) - 1, wires[i][1])
        lis[idx] = wires[i][1]

print(N - len(lis))

# https://www.acmicpc.net/board/view/8218
# 10
# 1 6
# 2 8
# 3 2
# 4 9
# 5 5
# 6 10
# 7 4
# 8 1
# 9 7
# 10 3
# => 6
