from unittest import TestCase


def solution(n):
    # 한번에 채우는 갯수는
    # n + (n - 1) + (n - 2)
    # 채운 후에 n 은 3씩 감소
    y_start = 0
    y_end = n - 1
    x_start = 0
    x_end = 0

    # n 의 원본 값을 기억하기 위한 변수
    origin_n = n
    arr = [[0] * i for i in range(1, n + 1)]
    cnt = 1

    while n > 0:
        # 위에서 아래로
        # n 회 반복
        for i in range(y_start, y_start + n):
            arr[i][x_start] = cnt
            cnt += 1

        # y 축 시작 위치는
        # 채운 후에 2씩 증가
        y_start += 2
        # x 축 시작 위치는
        # 채운 후에 1씩 증가
        x_start += 1

        # 아래에서 우측으로
        # n - 1 회 반복
        for i in range(n - 1):
            arr[y_end][x_start + i] = cnt
            cnt += 1

        # 우측에서 위로
        # n - 2회 반복
        for i in range(y_end - 1, y_end - 1 - (n - 2), -1):
            arr[i][i - x_end] = cnt
            cnt += 1

        # y 축의 끝 위치는
        # 채운 후에 1씩 감소
        y_end -= 1
        # x 축의 끝 위치는
        # 채운 후에 1씩 감소
        x_end += 1
        # 3 방향 모두 채운 후에
        # level 은 3씩 감소
        n -= 3

    answer = []

    for i in range(origin_n):
        for j in range(len(arr[i])):
            answer.append(arr[i][j])

    return answer


class SolutionTest(TestCase):
    def test_solution(self):
        self.assertEqual([1, 2, 9, 3, 10, 8, 4, 5, 6, 7], solution(4))

    def test_solution2(self):
        self.assertEqual([1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9], solution(5))
