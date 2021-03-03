N = int(input())
memo = [1, 2] + [0] * 999998
for i in range(2, 1000000):
    memo[i] = (memo[i - 2] + memo[i - 1]) % 15746
print(memo[N - 1])

# 참고
# https://sungmin-joo.tistory.com/21
# https://chancoding.tistory.com/23
