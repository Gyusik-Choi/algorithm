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

    def is_head_empty(self):
        if self.head.val is None:
            print("Tree is empty")
            return True
        return False

    def search(self, item):
        if self.is_head_empty():
            return False
        return self.search_node(self.head, item)

    def search_node(self, cur, item):
        if cur.val == item:
            return True

        if cur.val > item:
            return self.search_node(cur.left_child, item)
        return self.search_node(cur.right_child, item)

    def add(self, item):
        if self.is_head_empty():
            self.head = Node(item)
        else:
            return self.add_node(self.head, item)

    def add_node(self, cur, item):
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
        if self.is_head_empty():
            return False

        if self.head.val == item:
            if self.head.left_child is None and self.head.right_child is None:
                self.head = Node(None)
            elif self.head.left_child is not None and self.head.right_child is None:
                self.head = self.head.left_child
            elif self.head.left_child is None and self.head.right_child is not None:
                self.head = self.head.right_child
            else:
                value = self.find_most_small_value_from_right_node(self.head.right_child)
                self.head.val = value
                return self.remove_node(self.head, self.head.right_child, value)
        else:
            if self.head.val > item:
                if self.head.left_child is not None:
                    return self.remove_node(self.head, self.head.left_child, item)
                else:
                    print("Can't find {}".format(item))
                    return False
            else:
                if self.head.right_child is not None:
                    return self.remove_node(self.head, self.head.right_child, item)
                else:
                    print("Can't find {}".format(item))
                    return False

    def remove_node(self, parent, cur, item):
        if cur.val == item:
            if cur.left_child is None and cur.right_child is None:
                if parent.left_child == item:
                    parent.left_child = None
                else:
                    parent.right_child = None
            elif cur.left_child is not None and cur.right_child is None:
                if parent.left_child == item:
                    parent.left_child = None
                else:
                    parent.right_child = None
            elif cur.left_child is None and cur.right_child is not None:
                if parent.left_child == item:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                value = self.find_most_small_value_from_right_node(cur.right_child)
                cur.val = value
                return self.remove_node(cur, cur.right_child, value)
        else:
            if cur.val > item:
                if cur.left_child is not None:
                    return self.remove_node(cur, cur.left_child, item)
                else:
                    print("Can't find {}".format(item))
                    return False
            else:
                if cur.right_child is not None:
                    return self.remove_node(cur, cur.right_child, item)
                else:
                    print("Can't find {}".format(item))
                    return False

    def find_most_small_value_from_right_node(self, cur):
        if cur.left_child is None:
            return cur.val
        return self.find_most_small_value_from_right_node(cur.left_child)

    def pre_order(self):
        if self.is_head_empty():
            return False
        return self.pre_order_traverse(self.head)

    def pre_order_traverse(self, cur):
        self.pre_order_list.append(cur.val)

        if cur.left_child is not None:
            self.pre_order_traverse(cur.left_child)

        if cur.right_child is not None:
            self.pre_order_traverse(cur.right_child)

    def get_pre_order_list(self):
        self.pre_order()
        return self.pre_order_list

    def empty_pre_order_list(self):
        self.pre_order_list = []

    def in_order(self):
        if self.is_head_empty():
            return False
        return self.in_order_traverse(self.head)

    def in_order_traverse(self, cur):
        if cur.left_child is not None:
            self.in_order_traverse(cur.left_child)

        self.in_order_list.append(cur.val)

        if cur.right_child is not None:
            self.in_order_traverse(cur.right_child)

    def get_in_order_list(self):
        self.in_order()
        return self.in_order_list

    def empty_in_order_list(self):
        self.in_order_list = []

    def post_order(self):
        if self.is_head_empty():
            return False
        self.post_order_traverse(self.head)

    def post_order_traverse(self, cur):
        if cur.left_child is not None:
            self.post_order_traverse(cur.left_child)

        if cur.right_child is not None:
            self.post_order_traverse(cur.right_child)

        self.post_order_list.append(cur.val)

    def get_post_order_list(self):
        self.post_order()
        return self.post_order_list

    def empty_post_order_list(self):
        self.post_order_list = []


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

print(bt.get_in_order_list())
bt.empty_in_order_list()

bt.remove(10)
print(bt.get_in_order_list())

print(bt.get_pre_order_list())
print(bt.get_post_order_list())