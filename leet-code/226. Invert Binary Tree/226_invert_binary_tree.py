class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return

    invert_tree(root.left)
    invert_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)
print(invert_tree(tree))
