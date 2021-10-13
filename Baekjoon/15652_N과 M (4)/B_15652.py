def permutation(idx):
    if idx == M:
        print(' '.join(perm[:]))
    else:
        for i in range(N):
            if perm:
                if int(perm[-1]) <= arr[i]:
                    perm.append(str(arr[i]))
                    permutation(idx + 1)
                    perm.pop()
            else:
                perm.append(str(arr[i]))
                permutation(idx + 1)
                perm.pop()


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
perm = []
permutation(0)
