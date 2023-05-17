N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
for i in range(N):
    dp[i] = consult[i][1]

# for i in range(1, N):
# 위처럼 할 경우 0번 인덱스를 검사하지 못한다
#
# 바로 아래의 if 문의 의도는 상담이 안되는 날짜는
# dp 배열의 인덱스 값을 0으로 해서
# 추후 for 문을 다 돌고 dp 배열에서 최대 값을 구할때
# 추가적으로 상담 가능한 날인지 검사하지 않고
# 바로 max 함수로 답을 구하려는 의도였다
# for i in range(1, N) 은 0번 인덱스를
# 검사하지 못해서 0번 인덱스 날짜가 상담이 안되는 날짜일 수 있지만
# for 문의 대상 범위가 아니라
# 위에서 dp 값을 기본 상담 금액으로 세팅한 값이
# 상담이 안되는 날짜더라도 0으로 바뀌지 못한다
for i in range(N):
    if i + consult[i][0] > N:
        dp[i] = 0
        continue

    for j in range(i):
        if i - j < consult[j][0]:
            continue

        if consult[i][1] + dp[j] <= dp[i]:
            continue

        dp[i] = max(consult[i][1] + dp[j], dp[i])

print(max(dp))

# 반례 참고
# https://www.acmicpc.net/board/view/68114
