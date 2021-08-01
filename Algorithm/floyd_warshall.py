import copy


INF = float('inf')
N = 4
routes = [[0, 5, INF, 8], [7, 0, 9, INF], [2, INF, 0, 4], [INF, INF, 3, 0]]
answer = copy.deepcopy(routes)

for k in range(N):
    for i in range(N):
        for j in range(N):
            answer[i][j] = min(answer[i][j], answer[i][k] + answer[k][j])

print(answer)
