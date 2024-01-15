from typing import Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        sums = 0

        while stack:
            node = stack.pop()

            if node is None:
                continue

            if low <= node.val <= high:
                sums += node.val

            # 3번째 풀이와 달리
            # 범위에 포함되는 노드만 stack 에 넣는다
            #
            # 3번째 풀이는
            # 재귀 호출에 의해 계속 호출이 이어지기 때문에
            # 범위에 안 맞는 노드는 제거하고 호출이 이어지도록 해야한다
            #
            # 반면에 여기서는 스택에 넣는 노드만 탐색이 가능해서
            # 범위에 맞는 노드만 스택에 넣어야 한다
            if node.val > low:
                stack.append(node.left)

            if node.val < high:
                stack.append(node.right)

        return sums


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.tree = TreeNode(10)

    def test_range_sum_bst(self):
        self.tree.left = TreeNode(5)
        self.tree.left.left = TreeNode(3)
        self.tree.left.right = TreeNode(7)
        self.tree.right = TreeNode(15)
        self.tree.right.right = TreeNode(18)

        answer = self.solution.range_sum_bst(self.tree, 7, 15)
        self.assertEqual(answer, 32)

    def test_range_sum_bst2(self):
        self.tree.left = TreeNode(5)
        self.tree.left.left = TreeNode(3)
        self.tree.left.right = TreeNode(7)
        self.tree.left.left.left = TreeNode(1)
        self.tree.left.right.left = TreeNode(6)
        self.tree.right = TreeNode(15)
        self.tree.right.left = TreeNode(13)
        self.tree.right.right = TreeNode(18)

        answer = self.solution.range_sum_bst(self.tree, 6, 10)
        self.assertEqual(answer, 23)
