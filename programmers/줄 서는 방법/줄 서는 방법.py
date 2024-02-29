def solution(n, k):
    def get_factorial(target):
        fac = 1
        for t in range(target, 1, -1):
            fac *= t
        return fac

    answer = []
    arr = [i for i in range(1, n + 1)]

    while arr:
        factorial = get_factorial(n - 1)
        # (k - 1) // factorial 은
        # k // factorial - 1 과 다르다
        # ex>
        # (25 - 1) // 24 ==> 1
        # 25 // 24 - 1 ==> 0
        idx = (k - 1) // factorial
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
# https://hstory0208.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95
