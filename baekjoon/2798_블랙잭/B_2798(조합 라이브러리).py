def combination(k, n):
    if k == n:
        comb.append(lst[:])

    if not lst:
        idx = 0
    else:
        idx = cards.index(lst[-1]) + 1
    for i in range(idx, N):
        lst.append(cards[i])
        combination(k + 1, n)
        lst.pop()


N, M = map(int, input().split())
cards = list(map(int, input().split()))
lst = []
comb = []
combination(0, 3)

max_num = 0
for c in comb:
    if sum(c) <= M:
        if max_num < sum(c):
            max_num = sum(c)

print(max_num)
