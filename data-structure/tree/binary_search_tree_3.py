class Node:
    def __init__(self, item, left_child=None, right_child=None):
        self.val = item
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)

        self.pre_order_list = []
        self.in_order_list = []
        self.post_order_list = []

    def search(self, item):
        if self.head.val is None:
            return False

        if self.head.val == item:
            return True
        return self.search_node(self.head, item)

    def search_node(self, cur, item):
        if cur.val == item:
            return True

        if cur.val > item:
            if cur.val.left_child is not None:
                return self.search_node(cur.left_child, item)
            return False
        else:
            if cur.val.right_child is not None:
                return self.search_node(cur.right_child, item)
            return False

    def add(self, item):
        if self.head.val is None:
            self.head = Node(item)
        else:
            self.add_node(self.head, item)

    def add_node(self, cur, item):
        # 중복된 노드는 더하지 않는 방식으로 진행
        # 이진탐색트리는 탐색에 최적화되어 있는 자료구조인 만큼 특정 아이템의 갯수 보다는 특정 아이템을 더욱 빨리 찾을 수 있도록 중복된 노드는 추가하지 않는 방식으로 진행할 예정
        # 만약에 갯수를 파악하고 싶다면 노드를 추가하기 보다는 해당 노드의 갯수를 세는 프로퍼티를 추가하고 해당 노드의 갯수가 몇개인지 세어주는 방식이 나을 듯 하다
        if cur.val > item:
            if cur.left_child is None:
                cur.left_child = Node(item)
            else:
                return self.add_node(cur.left_child, item)
        else:
            if cur.right_child is None:
                cur.right_child = Node(item)
            else:
                return self.add_node(cur.right_child, item)

    def remove(self, item):
        if self.head.val is None:
            print("Tree is empty")
            return False

        if self.head.val == item:
            if self.head.left_child is None and self.head.right_child is None:
                self.head = Node(None)
            elif self.head.left_child is not None and self.head.right_child is None:
                self.head = self.head.left_child
            elif self.head.left_child is None and self.head.right_child is not None:
                self.head = self.head.right_child
            else:
                # item 과 교체할 숫자 value
                value = self.find_most_small_val_from_right_child(self.head.right_child)
                # value 를 트리에서 삭제한다
                self.remove_node(self.head, self.head.right_child, value)
                # item 을 value 로 바꿔준다
                self.head.val = value
        else:
            if self.head.val > item:
                return self.remove_node(self.head, self.head.left_child, item)
            else:
                return self.remove_node(self.head, self.head.right_child, item)

    def remove_node(self, parent, cur, item):
        if cur is None:
            print("Can't find {}".format(item))
            return False

        if cur.val == item:
            if cur.left_child is None and cur.right_child is None:
                if parent.left_child == cur:
                    parent.left_child = None
                else:
                    parent.right_child = None
            elif cur.left_child is not None and cur.right_child is None:
                cur = cur.left_child
            elif cur.left_child is None and cur.right_child is not None:
                cur = cur.right_child
            else:
                # cur 이 아니라 cur.right_child 를 인자로 넣어줘야 한다
                # item 과 교체할 숫자 value
                value = self.find_most_small_val_from_right_child(cur.right_child)
                # value 를 트리에서 삭제한다
                self.remove_node(cur, cur.right_child, value)
                # item 을 value 로 바꿔준다
                cur.val = value
        else:
            if cur.val > item:
                return self.remove_node(cur, cur.left_child, item)
            else:
                return self.remove_node(cur, cur.right_child, item)

    def find_most_small_val_from_right_child(self, cur):
        if cur.left_child is None:
            return cur.val
        return self.find_most_small_val_from_right_child(cur.left_child)

    def pre_order(self):
        cur = self.head
        if cur.val is None:
            print("Nothing to traverse")
            return False
        return self.pre_order_traverse(cur)

    def pre_order_traverse(self, cur):
        self.pre_order_list.append(cur.val)
        print(cur.val)

        if cur.left_child:
            self.pre_order_traverse(cur.left_child)

        if cur.right_child:
            self.pre_order_traverse(cur.right_child)

    def in_order(self):
        cur = self.head
        if cur.val is None:
            print("Nothing to traverse")
            return False
        return self.in_order_traverse(cur)

    def in_order_traverse(self, cur):
        if cur.left_child:
            self.in_order_traverse(cur.left_child)

        self.in_order_list.append(cur.val)
        print(cur.val)

        if cur.right_child:
            self.in_order_traverse(cur.right_child)

    def post_order(self):
        cur = self.head
        if cur.val is None:
            print("Nothing to traverse")
            return False
        return self.post_order_traverse(cur)

    def post_order_traverse(self, cur):
        if cur.left_child:
            self.post_order_traverse(cur.left_child)

        if cur.right_child:
            self.post_order_traverse(cur.right_child)

        self.post_order_list.append(cur.val)
        print(cur.val)


bt = BinarySearchTree()
bt.add(5)
bt.add(1)
bt.add(10)
bt.add(7)
bt.add(6)
bt.add(9)
bt.add(15)
bt.add(12)
bt.add(17)
bt.in_order()
bt.remove(10)
bt.in_order()

# 참고
# https://hongku.tistory.com/160
