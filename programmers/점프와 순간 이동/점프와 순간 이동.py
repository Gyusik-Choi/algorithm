import sys
sys.setrecursionlimit(10 ** 5)


def solution(n):
    # 목표 거리
    target_distance = n
    # 최소 소비량
    min_usage = n

    # 현재 위치, 현재 소비량
    def brute_force(distance, usage):
        nonlocal min_usage

        if distance > target_distance:
            return

        if distance == target_distance:
            min_usage = min(min_usage, usage)
            return

        # 점프
        brute_force(distance + 1, usage + 1)
        if distance:
            # 순간 이동
            brute_force(distance + distance, usage)

    brute_force(0, 0)
    return min_usage


# print(solution(5))
# print(solution(6))
print(solution(5000))

# 5
# 0 -> 1 점프
# 1 -> 2 순간 이동
# 2 -> 4 순간 이동
# 4 -> 1 점프
