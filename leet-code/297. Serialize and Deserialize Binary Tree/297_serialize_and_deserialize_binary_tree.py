from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode):
        if root is None:
            return '#'

        # 교재는 1번 인덱스부터 시작하기 위해
        # lst = ['#'] 로 했으나
        # 여기서는 0번 인덱스부터 시작하기 위해
        # 빈 리스트로 설정했다
        lst = []
        deq = deque([root])

        while deq:
            tree = deq.popleft()

            if tree:
                lst.append(str(tree.val))
                deq.append(tree.left)
                deq.append(tree.right)
            else:
                # 파이썬은 None 을 문자열로 바꿀 수 없어서
                # 교재의 방식에 따라 '#' 를 append 한다
                lst.append('#')

        # 마지막 자식 노드에서 left, right 에 대해
        # '#' 를 append 하기 때문에
        # 리스트의 맨 뒤에 '#' 가 있어서
        # rstrip 으로 이를 제거한다
        return ' '.join(lst).rstrip(' # ')

    def deserialize(self, data: str):
        if data == '#':
            return None

        nodes = data.split()
        # 교재와 달리 0번 인덱스부터 시작하기 때문에
        # 0번 인덱스 값을 가져온다
        root = TreeNode(int(nodes[0]))
        deq = deque([root])
        # 0번 인덱스부터 시작하기 때문에
        # 1번 인덱스부터 자식 노드다
        idx = 1

        while deq:
            node = deq.popleft()

            if idx < len(nodes) and nodes[idx] != '#':
                node.left = TreeNode(int(nodes[idx]))
                deq.append(node.left)
            idx += 1

            if idx < len(nodes) and nodes[idx] != '#':
                node.right = TreeNode(int(nodes[idx]))
                deq.append(node.right)
            idx += 1

        return root


vertex = TreeNode(1)
vertex.left = TreeNode(2)
vertex.right = TreeNode(3)
vertex.right.left = TreeNode(4)
vertex.right.right = TreeNode(5)
ser = Codec()
deser = Codec()
print(deser.deserialize(ser.serialize(vertex)))

vertex2 = TreeNode(None)
ser2 = Codec()
deser2 = Codec()
print(deser2.deserialize(ser2.serialize(vertex2)))

# 참고
# 파이썬 알고리즘 인터뷰
