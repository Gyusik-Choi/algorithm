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

# 참고
# https://blog.naver.com/ndb796/221234427842
# https://ssungkang.tistory.com/entry/Algorithm-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%99%80%EC%83%ACFloyd-Warshall-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
