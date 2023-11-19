from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    deq = deque([root])

    while deq:
        # 큐가 아닌
        # 스택으로 풀이할 경우 popleft 대신 pop 으로 수정할 수 있다
        # node = deq.pop()
        node = deq.popleft()

        if node:
            node.left, node.right = node.right, node.left
            deq.append(node.left)
            deq.append(node.right)

    return root


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)
print(invert_tree(tree))
