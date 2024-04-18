def solution(n, results):
    inf = float('inf')
    players = [[inf] * n for _ in range(n)]

    for i in range(n):
        players[i][i] = 0

    for a, b in results:
        players[a - 1][b - 1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                players[i][j] = min(players[i][j], players[i][k] + players[k][j])

    cnt = 0
    for i in range(n):
        flag = True
        for j in range(n):
            if players[i][j] == inf and players[j][i] == inf:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
