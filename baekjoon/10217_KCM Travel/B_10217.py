import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # M 비용 이하면서 최단 시간(d)
    N, M, K = map(int, sys.stdin.readline().split())
    routes = {i: [] for i in range(1, N + 1)}
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        routes[u].append([v, c, d])

    INF = float('inf')
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[1][0] = 0

    for cost in range(M + 1):
        for node in range(1, N + 1):
            if dp[node][cost] != INF:
                for end, value, time in routes[node]:
                    if cost + value <= M:
                        dp[end][cost + value] = min(dp[end][cost + value], dp[node][cost] + time)

    if min(dp[N]) != INF:
        sys.stdout.write(str(min(dp[N])) + "\n")
    else:
        sys.stdout.write("Poor KCM" + "\n")


# 참고
# https://maivve.tistory.com/226
# https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-10217%EB%B2%88-KCM-Travel-Java-Python
# https://developmentdiary.tistory.com/401
# https://kibbomi.tistory.com/178
# https://kyunstudio.tistory.com/160
# https://roamingman.tistory.com/m/46
