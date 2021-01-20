def combination(idx, m):
    global comb
    if idx == m:
        print(' '.join(comb))
    else:
        for j in range(N):
            if not check[j]:
                check[j] = True
                comb.append(str(arr[j]))
                combination(idx + 1, m)
                check[j] = False
                comb.pop()


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
comb = []
check = [0] * N
combination(0, M)
