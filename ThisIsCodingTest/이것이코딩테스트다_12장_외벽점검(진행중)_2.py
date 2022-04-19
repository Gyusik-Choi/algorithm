def solution(n, weak, dist):
    min_cnt = 0
    dist.sort(reverse=True)
    possible_check_points = [()]

    for d in dist:
        min_cnt += 1
        temp_possible_check_points = []

        for i, w in enumerate(weak):
            start = w
            end = weak[i:]

            for we in weak[:i]:
                end.append(n + we)

            candidate = []
            for e in end:
                if e - start <= d:
                    candidate.append(e % n)

            temp_possible_check_points.append(set(candidate))

        candidates = set()
        for p in possible_check_points:
            for t in temp_possible_check_points:
                new_candidate = t | set(p)

                if len(new_candidate) == len(weak):
                    return min_cnt

                candidates.add(tuple(new_candidate))

        possible_check_points = candidates

    return -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))

# print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))
# => 3
# print(solution(50, [1], [6]))
# => 1
# print(solution(30, [0, 3, 11, 21], [10, 4]))
# => 2
# print(solution(200, [0, 100], [1, 1]))
# => 2
# print(solution(12, [10, 0], [1, 2]))
# => 1
# print(solution(19, [0, 10], [9]))
# => 1
# print(solution(200, [1, 3, 5, 7, 9, 11], [1, 1, 1, 1, 1]))
# => -1
# print(solution(12, [4], [1, 2]))
# => 1
# print(solution(30, [0, 3, 11, 21], [10, 4]))
# => 2

# print(solution(200, [0, 30, 70, 80, 120, 160], [1, 10, 5, 40, 30]))

# 반례 찾았다!
# => dist 긴 순서대로만 볼게 아니라 조합으로 모든 케이스를 고려해야 한다

# https://velog.io/@tjdud0123/외벽-점검-2020-카카오-공채-python
# => 그러나 이분의 코드는 내가 했던 것처럼 dist 긴 순으로 했는데 해결했다
print(solution(300, [0, 10, 50, 80, 150, 160, 210, 250], [40, 30, 10, 10, 5, 1]))
# => 4

# 이 코드는 위의 링크를 참고해서 작성한 코드다
# 아직 제대로 이해하지 못해서 추가 학습이 필요하다
