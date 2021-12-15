from collections import deque


class Node:
    def __init__(self, item, left_child=None, right_child=None):
        self.val = item
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)

        self.pre_order_list = []

    def add(self, item):
        if self.head.val is None:
            self.head = Node(item)
        else:
            return self.add_node(self.head, item)

    def add_node(self, cur, item):
        if cur.val == item:
            print("We already have {}".format(item))
            return True

        if cur.val > item:
            if not cur.left_child:
                cur.left_child = Node(item)
                return True
            return self.add_node(cur.left_child, item)
        else:
            if not cur.right_child:
                cur.right_child = Node(item)
                return True
            return self.add_node(cur.right_child, item)

    def pre_order(self):
        if self.head.val is None:
            return False
        return self.pre_order_traverse(self.head)

    def pre_order_traverse(self, cur):
        self.pre_order_list.append(cur.val)

        if cur.left_child:
            self.pre_order_traverse(cur.left_child)

        if cur.right_child:
            self.pre_order_traverse(cur.right_child)

    def get_pre_order_list(self):
        self.pre_order()
        return self.pre_order_list

    def empty_pre_order_list(self):
        self.pre_order_list = []

    def invert_tree(self):
        deq = deque()
        root = self.head

        deq.append(root)
        while deq:
            node = deq.popleft()
            if node:
                node.left_child, node.right_child = node.right_child, node.left_child

                deq.append(node.left_child)
                deq.append(node.right_child)


bt = BinarySearchTree()
bt.add(4)
bt.add(2)
bt.add(7)
bt.add(1)
bt.add(3)
bt.add(6)
bt.add(9)
bt.add(10)
print(bt.get_pre_order_list())
bt.empty_pre_order_list()
bt.invert_tree()
print(bt.get_pre_order_list())

# 참고
# https://velog.io/@injoon2019/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%B0%98%EC%A0%84
# '파이썬 알고리즘 인터뷰' p.400
