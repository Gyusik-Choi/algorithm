n = int(input())
wine = [0]
for _ in range(n):
    w = int(input())
    wine.append(w)

dp = [0] * (n + 1)
dp[1] = wine[1]
if n > 1:
    dp[2] = max(wine[1], wine[1] + wine[2])
    if n > 2:
        # wine[1] + wine[2] 이 조건도 있어야 한다
        # 이 조건을 생각안해서 계속 오답이 났다
        # 3번째 잔까지의 최대값이 1번째 잔과 2번째 잔의 합일수도 있기 때문이다
        dp[3] = max(wine[1] + wine[2], wine[1] + wine[3], wine[2] + wine[3])
        if n > 3:
            for i in range(4, n + 1):
                dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
                # 이 if 문 조건이 없으면
                # 문제에서 예제로 주어진 6 6 10 13 9 8 1 은 [6, 10, 16, 23, 28, 33, 32] 인데
                # 7 6 10 13 9 8 1 0 이 주어졌다고 하면 [7, 10, 16, 23, 28, 33, 32, 32] 가 되므로 옳지 않다
                # [7, 10, 16, 23, 28, 33, 33, 33]이 되야 하기 때문에 필요한 조건문이다
                if dp[i] < dp[i - 1]:
                    dp[i] = dp[i - 1]

print(dp[n])
