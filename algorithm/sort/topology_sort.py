from collections import deque
from unittest import TestCase


def topology_sort(edges, level):
    deq = deque()

    for i in range(1, len(level)):
        if level[i] == 0:
            deq.append(i)

    result = []
    while deq:
        s = deq.popleft()

        for node in edges[s]:
            level[node] -= 1
            if level[node] == 0:
                deq.append(node)

        result.append(s)

    return result


class TopologySortTest(TestCase):
    def test_topology_test(self):
        # 입력 케이스
        # 7 8
        # 1 2
        # 1 5
        # 2 3
        # 2 6
        # 3 4
        # 4 7
        # 5 6
        # 6 4
        # => 1 2 5 3 6 4 7
        #
        # 정점, 간선 갯수
        v, e = map(int, input().split())
        edges_info = {i: [] for i in range(1, v + 1)}
        level_info = [0] * (v + 1)

        for _ in range(e):
            start, end = map(int, input().split())
            edges_info[start].append(end)
            level_info[end] += 1

        answer = topology_sort(edges_info, level_info)

        self.assertEquals(answer, [1, 2, 5, 3, 6, 4, 7])

# 참고
# 이것이 코딩 테스트다 (나동빈)
