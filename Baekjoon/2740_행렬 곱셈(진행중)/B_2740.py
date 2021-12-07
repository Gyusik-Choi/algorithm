import sys


N, M1 = map(int, sys.stdin.readline().split())
a = []
for i in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

M2, K = map(int, sys.stdin.readline().split())
b = []
for i in range(M2):
    b.append(list(map(int, sys.stdin.readline().split())))

answer = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M1):
            answer[i][j] += a[i][k] * b[k][j]

for i in range(N):
    print(*answer[i])
# for i in range(N):
#     for j in range(K):
#         sys.stdout.write(str(answer[i][j]) + " ")
#     sys.stdout.write("\n")


# 행렬
# 고등학생 이후로 거의 본적이 없던 행렬을 오랫만에 다시 만나게 됐다
# 문제를 풀기에 앞서 행렬에 대해서 다시 학습해보려 한다
# 이름만 들어본 선형대수학이 행렬과 관련있는 분야라는 것도 처음 알게 됐다
# https://ko.wikipedia.org/wiki/%ED%96%89%EB%A0%AC
# https://gosamy.tistory.com/3

# 행렬곱셈
# 행렬 a(2 * 3)와 b(3 * 2)를 곱하면
# (2 * 2)의 행렬이 된다
# 행렬 곱셈한 결과는 앞 행렬의 행 크기 * 뒤 행렬의 열 크기가 된다
# 행렬 곱셈은 특정 조건이 성립해야 가능하다
# A(a * b) * B(c * d) A와 B 행렬을 곱하려면
# b와 c가 같아야 가능하다

# https://st-lab.tistory.com/245
# https://mathbang.net/562
# https://m.blog.naver.com/junhyuk7272/50128686426
