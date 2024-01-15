from typing import Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if root.val < low:
            # 여기서 return 을 사용해야
            # 맨 아래의 return 문이 호출되지 않는다
            #
            # return 문을 사용하지 않으면
            # 아래의 코드가 호출된 후
            # 맨 아래의 return 코드도 호출된다
            #
            # 위, 아래의 if 문은
            # 범위를 벗어나는 노드를 제외하기 위한 코드인데
            # return 문을 사용하지 않으면 해당 노드가
            # 맨 아래의 return 문에 의해 범위에 포함되게 된다
            return self.range_sum_bst(root.right, low, high)

        if root.val > high:
            return self.range_sum_bst(root.left, low, high)

        return root.val + self.range_sum_bst(root.left, low, high) + self.range_sum_bst(root.right, low, high)


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
