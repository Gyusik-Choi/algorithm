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
        else:
            return self.search_node(self.head, item)

    def search_node(self, cur, item):
        if cur.val == item:
            return True

        if cur.val > item:
            # 왼쪽 자식노드가 있을 경우
            if cur.left_child is not None:
                return self.search_node(cur.left, item)
            # 왼쪽 자식노드가 없을 경우
            else:
                return False
        else:
            # 오른쪽 자식노드가 있을 경우
            if cur.right_child is not None:
                return self.search_node(cur.right, item)
            # 오른쪽 자식노드가 없을 경우
            else:
                return False

    def add(self, item):
        if self.head.val is None:
            self.head = Node(item)
        else:
            return self.add_node(self.head, item)

    def add_node(self, cur, item):
        # 탐색의 효율을 위해서 중복된 노드는 허용하지 않는다
        # 반드시 그래야 하는 것은 아니나 정 필요하면 똑같은 노드를 여러개 만들기 보다는
        # 해당 노드의 숫자를 세어주는 변수를 이용하는게 낫다는 의견이 있다
        if cur.val == item:
            print("We already have {}".format(item))
            return False

        # left
        if cur.val > item:
            if cur.left_child is None:
                cur.left_child = Node(item)
            else:
                return self.add_node(cur.left_child, item)
        # right
        else:
            if cur.right_child is None:
                cur.right_child = Node(item)
            else:
                return self.add_node(cur.right_child, item)

    def remove(self, item):
        if self.head.val is None:
            print("Nothing to remove")
            return False

        if self.head.val == item:
            # 자식노드가 하나도 없는 경우
            if self.head.left_child is None and self.head.right_child is None:
                self.head = Node(None)

            # 왼쪽 자식노드만 있는 경우(오른쪽 자식노드는 없음)
            elif self.head.left_child is not None and self.head.right_child is None:
                self.head = self.head.left_child

            # 오른쪽 자식노드만 있는 경우(왼쪽 자식노드는 없음)
            elif self.head.left_child is None and self.head.right_child is not None:
                self.head = self.head.right_child

            # 왼쪽, 오른쪽 자식노드가 모두 있는 경우
            # 해당하는 값을 오른쪽 자식노드에서 가장 왼쪽 자식으로 바꿔준다
            # 그리고 바꿔준 값이 원래 위치하고 있는 노드를 찾아서 없앤다
            else:
                self.head.val = self.search_most_left_val_from_right_node(self.head.right).val
                self.remove_node(self.head, self.head.right_child, self.head.val)

        else:
            if self.head.val > item:
                return self.remove_node(self.head, self.head.left_child, item)
            else:
                return self.remove_node(self.head, self.head.right_child, item)

    def remove_node(self, parent, cur, item):
        if cur is None:
            print("Can't find {}".format(item))
            return

        if cur.val == item:
            # 자식노드가 하나도 없는 경우
            if cur.left_child is None and cur.right_child is None:
                # 연결리스트 형태로 연결됐기 때문에 cur 의 상위 노드인 parent 로부터 cur 와의 연결고리를 끊어야 한다
                # 다만 parent 에서 cur 가 left 인지 right 인지 모르기 때문에 조건문으로 분기해서 처리한다
                if parent.left_child == cur:
                    parent.left_child = None
                else:
                    parent.right_child = None

            # 왼쪽 자식노드만 있는 경우(오른쪽 자식노드는 없음)
            elif cur.left_child is not None and cur.right_child is None:
                cur = cur.left_child

            # 오른쪽 자식노드만 있는 경우(왼쪽 자식노드는 없음)
            elif cur.left_child is None and cur.right_child is not None:
                cur = cur.right_child

            # 왼쪽, 오른쪽 자식노드가 모두 있는 경우
            # 해당하는 값을 오른쪽 자식노드에서 가장 왼쪽 자식으로 바꿔준다
            # 그리고 바꿔준 값이 원래 위치하고 있는 노드를 찾아서 없앤다
            else:
                cur.val = self.search_most_left_val_from_right_node(cur.right_child).val
                self.remove_node(cur, cur.right_child, cur.val)

        else:
            if cur.val > item:
                self.remove_node(cur, cur.left_child, item)
            else:
                self.remove_node(cur, cur.right_child, item)

    def search_most_left_val_from_right_node(self, cur):
        if cur.left_child is None:
            return cur
        else:
            return self.search_most_left_val_from_right_node(cur.left_child)

    # 전위순회(부모노드 -> 왼쪽자식 노드 -> 오른쪽자식 노드)
    def pre_order(self):
        if self.head.val is None:
            print("Nothing to traverse")
            return False
        return self.pre_order_traverse(self.head)

    def pre_order_traverse(self, cur):
        self.pre_order_list.append(cur.val)

        if cur.left_child:
            self.pre_order_traverse(cur.left_child)

        if cur.right_child:
            self.pre_order_traverse(cur.right_child)

    # 중위순회(왼쪽자식 노드 -> 부모노드 -> 오른쪽자식 노드)
    def in_order(self):
        if self.head.val is None:
            print("Nothing to traverse")
            return False
        return self.in_order_traverse(self.head)

    def in_order_traverse(self, cur):
        if cur.left_child:
            self.in_order_traverse(cur.left_child)

        self.in_order_list.append(cur.val)

        if cur.right_child:
            self.in_order_traverse(cur.right_child)

    # 후위순회(왼쪽자식 노드 -> 오른쪽자식 노드 -> 부모노드)
    def post_order(self):
        if self.head.val is None:
            print("Nothing to traverse")
            return False
        return self.post_order_traverse(self.head)

    def post_order_traverse(self, cur):
        if cur.left_child:
            self.post_order_traverse(cur.left_child)

        if cur.right_child:
            self.post_order_traverse(cur.right_child)

        self.post_order_list.append(cur.val)


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
bt.pre_order()
bt.remove(10)
bt.pre_order()

# 참고
# https://yaboong.github.io/data-structures/2018/02/12/binary-search-tree/ (중복에 관한 내용)
# https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/
# https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/BinaryTree.py
