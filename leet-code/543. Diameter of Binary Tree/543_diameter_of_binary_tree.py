class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
    longest = 0

    def dfs(vertex):
        nonlocal longest

        if not vertex:
            return -1

        left = dfs(vertex.left)
        right = dfs(vertex.right)

        longest = max(longest, left + right + 2)
        return max(left, right) + 1

    dfs(root)
    return longest


node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right = TreeNode(3)
print(diameter_of_binary_tree(node))

# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
# => 8
