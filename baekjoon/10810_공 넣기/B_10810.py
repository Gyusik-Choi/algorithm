N, M = map(int, input().split())
basket = [0] * (N + 1)
for _ in range(M):
    i, j, k = map(int, input().split())

    for idx in range(i, j + 1):
        basket[idx] = k

for num in range(1, N + 1):
    print(basket[num], end=" ")
