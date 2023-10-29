class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    # 맨 마지막 자식 노드는 0을 리턴한다
    # 재귀 호출을 통해 최하단 노드로 내려가면
    # 0을 리턴하고 그 위의 노드부터 1씩 더해진다
    if root is None:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(max_depth(node))

# 참고
# https://devraphy.tistory.com/567
