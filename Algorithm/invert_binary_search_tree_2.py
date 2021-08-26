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

    def invert_binary_search_tree(self):
        if self.head.val is not None:
            self.do_invert_binary_search_tree(self.head)

    def do_invert_binary_search_tree(self, cur):
        if cur:
            # left_child 의 self.do_invert_binary_search_tree(cur.right_child) 가
            # 더 이상 cur 가 없을 때까지 실행된다
            # cur.right_child 의 마지막 요소에서 self.do_invert_binary_search_tree(cur.right_child) 가 실행되게 되면
            # 더 이상 cur 가 없어서 해당 깊이에서의 실행은 리턴되는게 없이 종료된다
            # 그리고 cur.right_child 의 마지막 요소에서 self.do_invert_binary_search_tree(cur.right_child) 가 종료됐으므로 이 이후로 넘어간다
            # right_child = self.do_invert_binary_search_tree(cur.left_child) 가 실행될 차례다
            # 이것도 self.do_invert_binary_search_tree(cur.left_child) 실행되면 그 다음 cur 가 없기에 리턴되는게 없이 종료된다
            # 그러면 left_child 에는 반대편 자식 노드인 right_child 의 값이 할당되고
            # right_child 에는 left_child 의 값이 할당되면서 서로 값이 바뀐다
            # 이 다음에는 left_child 와 right_child 의 상위 노드에서의 right_child 가 실행될 차례가 된다
            # 상위 노드의 left_child 가 끝났기에 right_child 가 실행될 차례다
            left_child = self.do_invert_binary_search_tree(cur.right_child)
            right_child = self.do_invert_binary_search_tree(cur.left_child)

            cur.left_child = left_child
            cur.right_child = right_child

            return cur

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


bt = BinarySearchTree()
bt.add(4)
bt.add(2)
bt.add(7)
bt.add(1)
bt.add(3)
bt.add(6)
bt.add(9)
print(bt.get_pre_order_list())
bt.empty_pre_order_list()

bt.invert_binary_search_tree()
print(bt.get_pre_order_list())

# 참고
# https://velog.io/@injoon2019/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC-%EB%B0%98%EC%A0%84
