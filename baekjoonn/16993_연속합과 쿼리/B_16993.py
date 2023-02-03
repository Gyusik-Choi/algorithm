import sys


class Node:
    inf_min = -float('inf')

    def __init__(self, left=inf_min, right=inf_min, max_val=inf_min, sums=0):
        self.left = left
        self.right = right
        self.max_val = max_val
        self.sums = sums


def max_query(start, end, idx, left, right) -> Node:
    if right < start or end < left:
        return Node()

    if left <= start and end <= right:
        return segment_tree[idx]

    mid = (start + end) // 2
    front = max_query(start, mid, idx * 2, left, right)
    back = max_query(mid + 1, end, idx * 2 + 1, left, right)
    return Node(max(front.left, front.sums + back.left),
                max(front.right + back.sums, back.right),
                max(max(front.max_val, back.max_val), front.right + back.left),
                front.sums + back.sums)


def init_segment_tree(start, end, idx) -> Node:
    if start == end:
        segment_tree[idx] = Node(numbers[start], numbers[start], numbers[start], numbers[start])
        return segment_tree[idx]

    mid = (start + end) // 2
    front = init_segment_tree(start, mid, idx * 2)
    back = init_segment_tree(mid + 1, end, idx * 2 + 1)
    segment_tree[idx] = Node(max(front.left, front.sums + back.left),
                             max(front.right + back.sums, back.right),
                             max(max(front.max_val, back.max_val), front.right + back.left),
                             front.sums + back.sums)
    return segment_tree[idx]


N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]
segment_tree = [Node()] * (N * 4)
init_segment_tree(0, N - 1, 1)

for i, query in enumerate(queries):
    sys.stdout.write(str(max_query(0, N - 1, 1, query[0] - 1, query[1] - 1).max_val) + "\n")

# 참고
# https://viyoung.tistory.com/149
