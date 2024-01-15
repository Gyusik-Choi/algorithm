from typing import Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 첫번째 풀이를 아래 코드처럼 줄일 수 있다
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        return ((root.val if low <= root.val <= high else 0) +
                self.range_sum_bst(root.left, low, high) +
                self.range_sum_bst(root.right, low, high))


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
