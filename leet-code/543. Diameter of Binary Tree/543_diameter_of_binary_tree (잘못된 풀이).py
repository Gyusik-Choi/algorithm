class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
    if root is None:
        return 0

    def search(vertex):
        if vertex is None:
            return 0

        left = search(vertex.left)
        right = search(vertex.right)
        return max(left, right) + 1

    return search(root.left) + search(root.right)


node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right = TreeNode(3)
print(diameter_of_binary_tree(node))

node2 = TreeNode(1)
node2.left = TreeNode(2)
print(diameter_of_binary_tree(node2))

# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
# => 8
