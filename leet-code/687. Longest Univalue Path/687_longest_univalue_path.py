class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_univalue_path(root):
    longest = 0

    def dfs(vertex):
        nonlocal longest

        if not vertex:
            return 0

        left = dfs(vertex.left)
        right = dfs(vertex.right)

        if vertex.left and vertex.left.val == vertex.val:
            left += 1
        else:
            left = 0

        if vertex.right and vertex.right.val == vertex.val:
            right += 1
        else:
            right = 0

        longest = max(longest, left + right)
        return max(left, right)

    dfs(root)
    return longest


node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(1)
node.left.right = TreeNode(1)
node.right = TreeNode(5)
node.right.right = TreeNode(5)
print(longest_univalue_path(node))

node2 = TreeNode(1)
node2.left = TreeNode(4)
node2.left.left = TreeNode(4)
node2.left.right = TreeNode(4)
node2.right = TreeNode(5)
node2.right.right = TreeNode(5)
print(longest_univalue_path(node2))
