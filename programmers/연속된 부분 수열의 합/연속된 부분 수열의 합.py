from unittest import TestCase
from collections import deque


def solution(sequence, k):
    sums = 0
    deq = deque()
    answer = [0, 0]
    min_length = len(sequence)

    for idx, num in enumerate(sequence):
        sums += num
        deq.append(idx)

        if sums > k:
            while sums > k:
                sums -= sequence[deq.popleft()]

        if sums == k:
            if min_length > deq[-1] - deq[0]:
                answer[0], answer[1] = deq[0], deq[-1]
                min_length = deq[-1] - deq[0]

    return answer


class SolutionTest(TestCase):
    def test_solution(self):
        self.assertEquals(solution([1, 2, 3, 4, 5], 7), [2, 3])

    def test_solution2(self):
        self.assertEquals(solution([1, 1, 1, 2, 3, 4, 5], 5), [6, 6])

    def test_solution3(self):
        self.assertEquals(solution([2, 2, 2, 2, 2], 6), [0, 2])
