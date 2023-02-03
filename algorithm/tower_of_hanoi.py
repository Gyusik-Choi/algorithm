def hanoi(n, start, stopover, destination):
    global cnt
    if n == 1:
        cnt += 1
        arr.append([start, destination])
    else:
        hanoi(n - 1, start, destination, stopover)
        cnt += 1
        arr.append([start, destination])
        hanoi(n - 1, stopover, start, destination)


N = int(input())
cnt = 0
arr = []
hanoi(N, '1', '2', '3')
print(cnt)
for i in range(len(arr)):
    print(' '.join(arr[i]))

# 백준 11729

# 참고
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi

