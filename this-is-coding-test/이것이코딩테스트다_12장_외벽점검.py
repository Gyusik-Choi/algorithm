def solution(n, weak, dist):
    min_cnt = 0
    dist.sort(reverse=True)

    # 아래 total_check_points 가 for 문을 돌아야 하는데
    # 만약에 total_check_points 의 초기값이 [] 라면 for 문을 아예 돌지 못하게 된다
    # 대신 [()]로 설정해서 ()로 for 문을 돌 수 있게 되어서 temp_check_points 의 값들이 연산될 수 있다
    total_check_points = [()]
    for d in dist:
        min_cnt += 1

        temp_check_points = []
        for i in range(len(weak)):
            weak_start = weak[i]
            new_weak = weak[i:]

            for w in weak[:i]:
                new_weak.append(w + n)

            temp_check_points_candidates = []
            for weak_end in new_weak:
                if weak_end - weak_start <= d:
                    # 처음에는 같은 출발점 요소를 비교한다
                    # weak 를 신경쓰지 않아도 된다
                    temp_check_points_candidates.append(weak_end % n)

            temp_check_points.append(set(temp_check_points_candidates))

        total_check_points_candidates = set()
        for previous in total_check_points:
            for now in temp_check_points:
                if len(set(previous) | now) == len(weak):
                    return min_cnt

                total_check_points_candidates.add(tuple(set(previous) | now))

        total_check_points = total_check_points_candidates

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
# => 3

# https://velog.io/@tjdud0123/외벽-점검-2020-카카오-공채-python
# 이분의 코드는 내가 했던 것처럼 dist 긴 순으로 했는데 해결했다
print(solution(300, [0, 10, 50, 80, 150, 160, 210, 250], [40, 30, 10, 10, 5, 1]))
# => 4

