def combination(idx, m):
    if idx == m:
        print(' '.join(comb[:]))
    else:
        for j in range(N):
            if not check[j]:
                if comb:
                    if int(comb[-1]) < arr[j]:
                        check[j] = True
                        comb.append(str(arr[j]))
                        combination(idx + 1, m)
                        check[j] = False
                        comb.pop()
                else:
                    check[j] = True
                    comb.append(str(arr[j]))
                    combination(idx + 1, m)
                    check[j] = False
                    comb.pop()


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
comb = []
check = [False] * N
combination(0, M)
