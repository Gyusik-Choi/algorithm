def knapsack(max_num, max_volume, volume, value):
    arr = [[0] * (max_volume + 1) for _ in range(max_num + 1)]
    for num in range(max_num + 1):
        for vol in range(max_volume + 1):
            if num == 0 or vol == 0:
                arr[num][vol] = 0
            elif volume[num - 1] <= vol:
                arr[num][vol] = max(value[num - 1] + arr[num - 1][vol - volume[num - 1]], arr[num - 1][vol])
            else:
                arr[num][vol] = arr[num - 1][vol]
    return arr[max_num][max_volume]


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    V = []
    C = []
    for i in range(N):
        a, b = map(int, input().split())
        V.append(a)
        C.append(b)
    ans = knapsack(N, K, V, C)
    print("#{} {}".format(t, ans))
