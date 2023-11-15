class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1


vertex = TreeNode(3)
vertex.left = TreeNode(9)
vertex.right = TreeNode(20)
vertex.right.left = TreeNode(15)
vertex.right.right = TreeNode(7)
solution = Solution()
print(solution.is_balanced(vertex))

vertex2 = TreeNode(1)
vertex2.left = TreeNode(2)
vertex2.right = TreeNode(2)
vertex2.left.left = TreeNode(3)
vertex2.left.right = TreeNode(3)
vertex2.left.left.left = TreeNode(4)
vertex2.left.left.right = TreeNode(4)
solution2 = Solution()
print(solution2.is_balanced(vertex2))

vertex3 = TreeNode()
solution3 = Solution()
print(solution3.is_balanced(vertex3))

vertex4 = TreeNode(1)
vertex4.left = TreeNode(2)
vertex4.right = TreeNode(3)
vertex4.left.left = TreeNode(4)
vertex4.left.right = TreeNode(5)
vertex4.right.left = TreeNode(6)
vertex4.left.left.left = TreeNode(8)
solution4 = Solution()
print(solution4.is_balanced(vertex4))
