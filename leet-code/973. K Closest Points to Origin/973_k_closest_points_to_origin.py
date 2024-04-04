import heapq
from typing import List
from unittest import TestCase


class Solution:
    def __get_dist(self, point: list[int]):
        return abs(point[0]) ** 2 + abs(point[1]) ** 2

    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            heapq.heappush(heap, [self.__get_dist(point), i])

        answer = []
        for _ in range(k):
            dist, i = heapq.heappop(heap)
            answer.append(points[i])

        return answer


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_k_closest(self):
        answer = self.solution.k_closest([[1, 3], [-2, 2]], 1)
        self.assertEqual(answer, [[-2, 2]])

    def test_k_closest_2(self):
        answer = self.solution.k_closest([[3, 3], [5, -1], [-2, 4]], 2)
        # 문제에서 정답 리스트에 담긴 순서는 상관 없다고 했다
        # 여기서는 검증을 위해 동일한 값이 있는지 보려고
        # sorted 함수로 정렬해서 비교했다
        # assertListEqual 메소드는
        # 해당 메소드는 리스트 요소의 순서가 서로 같은 경우만 같다고 판단한다
        self.assertEqual(sorted(answer), sorted([[3, 3], [-2, 4]]))
