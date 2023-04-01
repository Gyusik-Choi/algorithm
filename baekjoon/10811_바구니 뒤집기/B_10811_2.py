N, M = map(int, input().split())
basket = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())

    while i < j:
        basket[i], basket[j] = basket[j], basket[i]
        i, j = i + 1, j - 1

for b in range(1, N + 1):
    print(basket[b], end=" ")
