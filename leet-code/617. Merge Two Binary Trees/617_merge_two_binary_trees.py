class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1, root2):
    if root1 and root2:
        node = TreeNode(root1.val + root2.val)
        node.left = merge_trees(root1.left, root2.left)
        node.right = merge_trees(root1.right, root2.right)
        return node

    return root1 or root2


tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(5)
tree1.right = TreeNode(2)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.left.right = TreeNode(4)
tree2.right = TreeNode(3)
tree2.right.right = TreeNode(7)

print(merge_trees(tree1, tree2))
