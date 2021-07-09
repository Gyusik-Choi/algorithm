class Node:
    def __init__(self, item, left_child=None, right_child=None):
        self.val = item
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)

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
            cur.left_child, cur.right_child = self.do_invert_binary_search_tree(cur.right_child), self.do_invert_binary_search_tree(cur.left_child)


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
bt.invert_binary_search_tree()
