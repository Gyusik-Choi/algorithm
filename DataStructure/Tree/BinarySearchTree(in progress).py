# 이진트리와 이진탐색트리 차이
# 이진 트리란 노드의 최대차수가 2인 트리
# 이진 탐색트리는 이진트리에서 조건이 추가된 것
# 추가된 조건: 루트노드의 왼쪽 자식노드는 루트노드보다 작다
# 추가된 조건: 루트노드의 오른쪽 자식노드는 루트노드보다 크다.


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)

        self.pre_order_list = []

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.search_node(self.head, item)

    def search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.search_node(cur.right, item)
                else:
                    return False

    def add(self, item):
        if self.head.val is None:
            self.head = Node(item)
        else:
            self.add_item(self.head, item)

    def add_item(self, cur, item):
        # left
        if cur.val >= item:
            if cur.left is None:
                cur.left = Node(item)
            else:
                self.add_item(cur.left, item)
        # right
        else:
            if cur.right is None:
                cur.right = Node(item)
            else:
                self.add_item(cur.right, item)

    def remove(self, item):
        if self.head.val is None:
            print ("there is no item: in BST", item)
        if self.head.val == item:
            # 1) Node to be removed has no children.
            if self.head.left is None and self.head.right is None:
                self.head = None
            # 2) Node to be removed has one child.
            elif self.head.left is None and self.head.right is not None:
                self.head = self.head.right
            # 3) Node to be removed has one child.
            elif self.head.left is not None and self.head.right is None:
                self.head = self.head.left
            # 4) Node to be removed has two children.
            else:
                self.head.val = self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
        else:
            if self.head.val > item:
                self.__remove(self.head, self.head.left, item)
            else:
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print("There is no item: ", item)
        if cur.val == item:
            # 1) Node to be removed has no children.
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            # 2) Node to be removed has one child.
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
            # 3) Node to be removed has one child.
            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            # 4) Node to be removed has two children.
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)
        else:
            if cur.val > item:
                self.__remove(cur, cur.left, item)
            else:
                self.__remove(cur, cur.right, item)

    def __removeitem(self, parent, cur, item):
        if cur.val == item:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__removeitem(cur, cur.left, item)
            else:
                self.__removeitem(cur, cur.right, item)

    def __most_left_val_from_right_node(self, cur):
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left)

    def pre_order_traverse(self):
        if self.head is not None:
            self.pre_order(self.head)

    def pre_order(self, cur):
        self.pre_order_list.append(cur.val)
        print(cur.val)
        if cur.left is not None:
            self.pre_order(cur.left)
        if cur.right is not None:
            self.pre_order(cur.right)


bt = BinarySearchTree()
bt.add(5)
bt.add(3)
bt.add(4)
bt.add(2)
bt.add(6)
bt.add(8)
bt.add(7)
bt.pre_order_traverse()
bt.remove(7)
bt.pre_order_traverse()


# 참고
# https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/BinaryTree.py
# https://galid1.tistory.com/176
