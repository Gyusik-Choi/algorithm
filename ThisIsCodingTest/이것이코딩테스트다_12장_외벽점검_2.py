from itertools import permutations


def solution(n, weak, dist):
    # 2배 늘리기 전의 원래 weak 길이다
    weak_length = len(weak)
    min_cnt = len(dist) + 1

    # weak 배열의 길이를 2배로 늘리기
    for i in range(weak_length):
        weak.append(n + weak[i])

    # 원래 weak 길이로 탐색
    for weak_idx in range(weak_length):
        dist_permutations = list(permutations(dist, len(dist)))

        # dist 길이로 dist 의 순열 구한 값을 하나씩 탐색
        for dist_item in dist_permutations:
            cnt = 1

            # 탐색 가능한 범위 = 취약 지점 + 순열 요소의 점검 거리
            dist_area = weak[weak_idx] + dist_item[cnt - 1]

            for idx in range(weak_idx, weak_idx + weak_length):
                if dist_area < weak[idx]:
                    cnt += 1

                    # cnt 를 1로 시작해 순열 요소의 점검 거리 구할때 cnt - 1로 계산
                    # cnt == len(dist) 가 아니라 cnt > len(dist) 로 점검 가능한 인원 초과 여부 판단
                    if cnt > len(dist):
                        break

                    dist_area = weak[idx] + dist_item[cnt - 1]

            min_cnt = min(min_cnt, cnt)

    if min_cnt == len(dist) + 1:
        return -1

    return min_cnt


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

print(solution(300, [0, 10, 50, 80, 150, 160, 210, 250], [40, 30, 10, 10, 5, 1]))
# => 4

# 이 코드는 '이것이 코딩테스트다' 교재의 답안을 참고한 코드다
