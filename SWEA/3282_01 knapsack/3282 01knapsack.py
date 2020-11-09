def knapsack(n, w, wt, val):
    # n = N, w = K, wt = V, val = C
    arr = [[0] * (w + 1) for _ in range(n + 1)]
    for j in range(n + 1):
        for k in range(w + 1):
            if j == 0 or k == 0:
                arr[j][k] = 0
            elif wt[j - 1] <= k:
                arr[j][k] = max(val[j - 1] + arr[j - 1][k - wt[j - 1]], arr[j - 1][k])
            else:
                arr[j][k] = arr[j - 1][k]
    return arr[n][w]


T = int(input())
for t in range(1, T+1):
    # N: 최대 물건 수, K: 최대 부피
    N, K = map(int, input().split())
    # V: 1번 물건부터 N번 물건까지 부피, C: 1번 물건부터 N번 물건까지 가치
    V = []
    C = []
    for i in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)
    print("#{} {}".format(t, knapsack(N, K, V, C)))


# 참고
# https://gsmesie692.tistory.com/113