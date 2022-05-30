T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    gold = [[0] * m for _ in range(n)]
    number_of_gold = list(map(int, input().split()))

    i = 0
    for j in range(n * m):
        x = i
        y = j % m
        gold[x][y] = number_of_gold[j]
        if j == m * i + n:
            i += 1

    
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
