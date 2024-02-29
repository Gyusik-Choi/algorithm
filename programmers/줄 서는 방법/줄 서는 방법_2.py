def solution(n, k):
    def get_factorial(target):
        fac = 1
        for t in range(target, 1, -1):
            fac *= t
        return fac

    answer = []
    arr = [i for i in range(1, n + 1)]
    k -= 1
    while arr:
        factorial = get_factorial(n - 1)
        idx = k // factorial
        answer.append(arr.pop(idx))
        k = k % factorial
        n -= 1

    return answer


# print(solution(3, 5))
# print(solution(5, 34))
# print(solution(5, 25))
# print(solution(2, 2))
# print(solution(5, 120))
# print(solution(5, 48))
# print(solution(5, 49))

# 참고
# https://kangworld.tistory.com/258
