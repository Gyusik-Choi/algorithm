from typing import Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_diff_in_bst(self, root: Optional[TreeNode]) -> int:
        min_diff = 10 ** 5
        # traverse 함수 안에서 왼쪽 자식노드부터 탐색을 한다
        # 맨 아래 노드까지 내려가는데
        # 이때 prev 는 여기서 설정한 값이다
        # 맨 아래 노드가 비교 되어야 할 값은
        # 여기서 설정한 값이 아니라 맨 아래 노드의 부모 노드다
        # 맨 아래 노드가 여기서 설정한 값과 비교 되는걸 막을 순 없어서
        # 비교가 되더라도 위에서 설정한 min_diff 값 보다
        # 작아지는 경우가 없도록 해야 한다
        # 작아지는 경우가 없도록 하기 위해 min_diff 를 음수 값을 설정해서
        # cur.val - prev.val 을 했을 때 최소값이 min_diff 가 되도록 한다
        # 맨 아래 노드의 val 이 0 이면 min_diff 가 된다
        prev = TreeNode(-min_diff)

        def traverse(cur: Optional[TreeNode]):
            nonlocal min_diff, prev

            if cur is None:
                return

            traverse(cur.left)
            min_diff = min(min_diff, cur.val - prev.val)
            prev = cur
            traverse(cur.right)

        traverse(root)
        return min_diff


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right = TreeNode(6)

        answer = self.solution.min_diff_in_bst(tree)
        self.assertEqual(1, answer)

    def test_solution2(self):
        tree = TreeNode(1)
        tree.left = TreeNode(0)
        tree.right = TreeNode(48)
        tree.right.left = TreeNode(12)
        tree.right.right = TreeNode(49)

        answer = self.solution.min_diff_in_bst(tree)
        self.assertEqual(1, answer)

    def test_solution3(self):
        tree = TreeNode(90)
        tree.left = TreeNode(69)
        tree.left.left = TreeNode(49)
        tree.left.right = TreeNode(89)
        tree.left.left.right = TreeNode(52)

        answer = self.solution.min_diff_in_bst(tree)
        self.assertEqual(1, answer)

    def test_solution4(self):
        tree = TreeNode(27)
        tree.right = TreeNode(34)
        tree.right.right = TreeNode(58)
        tree.right.right.left = TreeNode(50)
        tree.right.right.left.left = TreeNode(44)

        answer = self.solution.min_diff_in_bst(tree)
        self.assertEqual(6, answer)

    def test_solution5(self):
        tree = TreeNode(99)
        tree.left = TreeNode(84)
        tree.left.left = TreeNode(27)
        tree.left.left.left = TreeNode(1)
        tree.left.left.right = TreeNode(53)

        answer = self.solution.min_diff_in_bst(tree)
        self.assertEqual(15, answer)
