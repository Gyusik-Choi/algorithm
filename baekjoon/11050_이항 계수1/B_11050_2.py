# 풀이 2
# 재귀를 통한 방법으로 풀이한다
# 메모이제이션은 다음 풀이에서 적용할 계획이다.
# 메모이제이션을 적용하지 않은 재귀이지만
# 최대 입력이 10이라 통과할 수 있을 것이라 생각했는데
# recursion limit 초과와
# recursion limit 늘려준 후에는 메모리 초과가 발생했다.


import sys
sys.setrecursionlimit(10 ** 6)


def binomial(n, k):
    if k == 0 or n == k:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)


N, K = map(int, input().split())
ans = binomial(N - 1, K - 1) + binomial(N - 1, K)
print(ans)
