import copy


def trace_route(s, e):
    if s + 1 == pi[s][e]:
        return
    trace_route(s, pi[s][e] - 1)
    print(pi[s][e], end=" ")


INF = float('inf')
N = 5
routes = [[0, 3, 8, INF, -4], [INF, 0, INF, 1, 7], [INF, 4, 0, INF, INF], [2, INF, -5, 0, INF], [INF, INF, INF, 6, 0]]
answer = copy.deepcopy(routes)
# 직전 정점 행렬
# pi[0][1]은 1에서 2로 갈때 2 직전에 들리는 정점
# 1에서 2로 갈때 바로 2로 갔는지 아니면 다른 곳을 어디어디 거쳐서 갔는지를 추적할 수 있음
pi = [[-1] * N for _ in range(N)]

for m in range(N):
    for n in range(N):
        if m != n and routes[m][n] != INF:
            pi[m][n] = m + 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if answer[i][j] > answer[i][k] + answer[k][j]:
                answer[i][j] = answer[i][k] + answer[k][j]
                pi[i][j] = pi[k][j]

for m in range(N):
    for n in range(N):
        if m != n:
            print("{} -> {} 경로 : ".format(m + 1, n + 1))
            print(m + 1, end=" ")
            trace_route(m, n)
            print(n + 1)
            print()

# 참고
# https://ssungkang.tistory.com/entry/Algorithm-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%99%80%EC%83%ACFloyd-Warshall-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# https://techbless.github.io/2020/11/11/C-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B5%AC%ED%98%84%EA%B3%BC-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%99%80%EC%83%AC-%EA%B2%BD%EB%A1%9C-%EC%B6%9C%EB%A0%A5-%EB%B0%A9%EB%B2%95/
# https://blog.naver.com/ndb796/221234427842
