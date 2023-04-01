N, M = map(int, input().split())
basket = [i for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())

    i -= 1
    j -= 1

    pre_reverse = i
    post_reverse = j + 1

    temp = []

    for k in range(pre_reverse):
        temp.append(basket[k])

    for k in range(j, i - 1, -1):
        temp.append(basket[k])

    for k in range(post_reverse, N):
        temp.append(basket[k])

    basket = temp

for b in basket:
    print(b + 1, end=" ")
