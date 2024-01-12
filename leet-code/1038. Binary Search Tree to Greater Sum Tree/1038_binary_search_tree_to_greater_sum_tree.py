from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 중위 순회
    # 오른쪽 자식노드 -> 부모노드 -> 왼쪽 자식노드
    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        sums = 0

        def dfs(vertex: Optional[TreeNode]):
            nonlocal sums

            if not vertex:
                return vertex

            dfs(vertex.right)
            vertex.val += sums
            sums = vertex.val
            dfs(vertex.left)
            return vertex

        return dfs(root)


node = TreeNode(4)
node.left = TreeNode(1)
node.left.left = TreeNode(0)
node.left.right = TreeNode(2)
node.left.right.right = TreeNode(3)
node.right = TreeNode(6)
node.right.left = TreeNode(5)
node.right.right = TreeNode(7)
node.right.right.right = TreeNode(8)
solution = Solution()
print(solution.bst_to_gst(node))
