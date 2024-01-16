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
        stack = [root]

        while stack:
            cur = stack.pop()

            if cur is None:
                continue

            most_left_node = None
            most_right_node = None

            if cur.left is not None:
                most_right_node = self.__find_most_right_child_node(cur.left)
                stack.append(cur.left)

            if cur.right is not None:
                most_left_node = self.__find_most_left_child_node(cur.right)
                stack.append(cur.right)

            if most_right_node is not None:
                min_diff = min(min_diff, cur.val - most_right_node.val)

            if most_left_node is not None:
                min_diff = min(min_diff, most_left_node.val - cur.val)

        return min_diff

    def __find_most_left_child_node(self, node):
        if node.left is None:
            return node
        return self.__find_most_left_child_node(node.left)

    def __find_most_right_child_node(self, node):
        if node.right is None:
            return node
        return self.__find_most_right_child_node(node.right)


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
