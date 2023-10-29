from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0

    cnt = 0
    deq = deque([root])

    while deq:
        cnt += 1

        for _ in range(len(deq)):
            vertex = deq.popleft()

            if vertex.left:
                deq.append(vertex.left)

            if vertex.right:
                deq.append(vertex.right)

    return cnt


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(max_depth(node))

# 참고
# 파이썬 알고리즘 인터뷰
