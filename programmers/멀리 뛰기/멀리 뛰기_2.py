def solution(n):
    # 1 -> 1 (1)
    # 2 -> 2 (1, 1), (2)
    # 3 -> 3
    # 4 -> 5
    # 5 -> 8
    # fibonacci

    # n 은 최대 2000 까지다
    # 만약에 2001 대신
    # (n + 1) 로 한다면
    # n 이 1일 경우
    # jumps[2] 에 접근하면
    # 인덱스 에러가 발생한다

    jumps = [0, 1, 2]

    for i in range(3, n + 1):
        jumps.append(jumps[-2] + jumps[-1])

    return jumps[n] % 1234567


print(solution(4))
print(solution(3))
print(solution(1))
