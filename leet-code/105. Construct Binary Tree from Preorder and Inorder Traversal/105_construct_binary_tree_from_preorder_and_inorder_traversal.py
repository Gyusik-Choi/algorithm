from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[idx])
            node.left = self.build_tree(preorder, inorder[:idx])
            node.right = self.build_tree(preorder, inorder[idx + 1:])
            return node
