from unittest import TestCase


class Node:
    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)

    def search(self, val: int) -> bool:
        if self.head.val is None:
            return False

        return self.__search(self.head, val)

    def __search(self, cur: Node, val: int) -> bool:
        if cur.val == val:
            return True

        # left
        if cur.val > val:
            if cur.left_child is None:
                return False
            return self.__search(cur.left_child, val)
        # right
        else:
            if cur.right_child is None:
                return False
            return self.__search(cur.right_child, val)

    def add(self, val: int) -> bool:
        if self.head.val is None:
            self.head.val = val
            return True
        return self.__add(self.head, val)

    def __add(self, cur: Node, val: int) -> bool:
        if cur.val == val:
            return False

        if cur.val > val:
            if cur.left_child is not None:
                return self.__add(cur.left_child, val)
            cur.left_child = Node(val)
        else:
            if cur.right_child is not None:
                return self.__add(cur.right_child, val)
            cur.right_child = Node(val)

        return True

    # remove 와 __remove 를 하나로 하고 싶었으나 아직 방법을 찾지 못했다
    # remove 와 __remove 는 유사하지만 차이가 있다
    # remove 의 경우 루트 노드에 제거하려는 값이 있는 경우라
    # 상위 노드 없이 루트 노드와 자식 노드 만으로 제거가 가능하다
    # __remove 의 경우 루트 노드가 아닌 자식 노드에 제거하려는 값이 있는 경우라
    # 부모 노드가 필요하다
    def remove(self, val: int) -> bool:
        if self.head.val is None:
            return False

        if self.head.val == val:
            # 1) 자식 노드가 둘 다 없는 경우
            if self.head.left_child is None and self.head.right_child is None:
                self.head = Node(None)
            # 2) 오른쪽 자식 노드만 있는 경우
            elif self.head.left_child is None:
                self.head = self.head.right_child
            # 3) 왼쪽 자식 노드만 있는 경우
            elif self.head.right_child is None:
                self.head = self.head.left_child
            # 4) 자식 노드가 둘 다 있는 경우
            else:
                # 오른쪽 자식 노드에서 가장 작은 값을 찾는다
                # (왼쪽 자식 노드에서 가장 큰 값을 찾는 방법을 사용할 수도 있다)
                right_smallest_node = self.__find_smallest_node_from_right_child(self.head.right_child)
                self.head.val = right_smallest_node.val
                # 오른쪽 자식 노드에서 가장 작은 값을 루트 노드로 옮겨 왔으니
                # 오른쪽 자식 노드에서 가장 작은 값을 트리에서 제거한다
                # (코드 상으로는 루트 노드로 옮겨 왔다기 보다는 루트 노드의 val 만
                # 오른쪽 자식 노드에서 가장 작은 노드의 val 로 대체 한거라
                # 오른쪽 자식 노드에서 가장 작은 노드는 트리에 아직 남아있어서
                # 이를 제거해야 한다)
                self.__remove(self.head, self.head.right_child, right_smallest_node.val)
            return True

        if self.head.val > val:
            return self.__remove(self.head, self.head.left_child, val)
        return self.__remove(self.head, self.head.right_child, val)

    def __remove(self, parent: Node, cur: Node, val: int) -> bool:
        if cur is None:
            return False

        if cur.val == val:
            # 1) 자식 노드가 둘 다 없는 경우
            if cur.left_child is None and cur.right_child is None:
                # if parent.left_child.val == cur.val
                # 위와 같은 조건문은 안 된다
                # left_child 가 None 이고
                # right_child.val 이 찾는 val 이면
                # left_child 는 None 이라 val 과 같은 요소가 없다
                # 아래와 같은 에러가 발생할 것이다
                # AttributeError: 'NoneType' object has no attribute 'val'
                if parent.left_child == cur:
                    parent.left_child = None
                else:
                    parent.right_child = None
            # 2) 오른쪽 자식 노드만 있는 경우
            elif cur.left_child is None:
                if parent.left_child == cur:
                    parent.left_child = cur.right_child
                else:
                    parent.right_child = cur.right_child
            # 3) 왼쪽 자식 노드만 있는 경우
            elif cur.right_child is None:
                if parent.left_child == cur:
                    parent.left_child = cur.left_child
                else:
                    parent.right_child = cur.left_child
            # 4) 자식 노드가 둘 다 있는 경우
            else:
                right_smallest_node = self.__find_smallest_node_from_right_child(cur.right_child)
                cur.val = right_smallest_node.val
                # self.__remove_right_smallest_node(cur, cur.right_child, right_smallest_node.val)
                self.__remove(cur, cur.right_child, cur.val)
            return True

        if cur.val > val:
            return self.__remove(cur, cur.left_child, val)
        return self.__remove(cur, cur.right_child, val)

    # 오른쪽 자식 노드 중 가장 작은 노드
    # 오른쪽 자식 노드부터 탐색을 할 수 있도록 파라미터인 cur 은
    # 탐색하려는 노드의 오른쪽 자식 노드가 와야 한다
    # 탐색은 가장 작은 노드를 찾아야 해서 왼쪽 자식 노드를 찾는다
    def __find_smallest_node_from_right_child(self, cur: Node) -> Node:
        if cur.left_child is None:
            return cur
        return self.__find_smallest_node_from_right_child(cur.left_child)

    # 전위 순회
    def traverse_pre_order(self) -> list:
        def __traverse(cur: Node, history: list[int]) -> list:
            if cur is None:
                return history

            history.append(cur.val)
            __traverse(cur.left_child, history)
            __traverse(cur.right_child, history)
            return history

        return __traverse(self.head, [])

    # 중위 순회
    def traverse_in_order(self) -> list:
        def __traverse(cur: Node, history: list[int]) -> list:
            if cur is None:
                return history

            __traverse(cur.left_child, history)
            history.append(cur.val)
            __traverse(cur.right_child, history)
            return history

        return __traverse(self.head, [])

    # 후위 순회
    def traverse_post_order(self) -> list:
        def __traverse(cur: Node, history: list[int]) -> list:
            if cur is None:
                return history

            __traverse(cur.left_child, history)
            __traverse(cur.right_child, history)
            history.append(cur.val)
            return history

        return __traverse(self.head, [])


class BinarySearchTreeTest(TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    # 아무 노드도 없는 경우
    def test_search(self):
        self.assertEqual(self.bst.search(1), False)

    # 루트 노드 값이 1인 경우
    def test_search2(self):
        self.bst.head.val = 1
        self.assertEqual(self.bst.search(1), True)

    def test_search3(self):
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)

        self.assertEqual(self.bst.search(1), True)
        self.assertEqual(self.bst.search(2), True)
        self.assertEqual(self.bst.search(3), True)

    def test_search4(self):
        self.bst.add(4)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)
        self.bst.add(6)
        self.bst.add(5)
        self.bst.add(7)

        self.assertEqual(self.bst.search(1), True)
        self.assertEqual(self.bst.search(2), True)
        self.assertEqual(self.bst.search(3), True)
        self.assertEqual(self.bst.search(4), True)
        self.assertEqual(self.bst.search(5), True)
        self.assertEqual(self.bst.search(6), True)
        self.assertEqual(self.bst.search(7), True)

    def test_remove(self):
        self.assertEqual(self.bst.remove(1), False)

    def test_remove2(self):
        self.bst.add(1)
        self.bst.remove(1)
        self.assertEqual(self.bst.search(1), False)

    def test_remove3(self):
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)

        self.bst.remove(2)
        self.assertEqual(self.bst.search(2), False)
        self.assertEqual(self.bst.head.val, 3)
        self.assertEqual(self.bst.head.left_child.val, 1)
        self.assertEqual(self.bst.head.right_child, None)

    def test_remove4(self):
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)

        self.bst.remove(1)
        self.assertEqual(self.bst.head.left_child, None)
        self.bst.remove(3)
        self.assertEqual(self.bst.head.right_child, None)

    def test_remove5(self):
        self.bst.add(3)
        self.bst.add(2)
        self.bst.add(1)

        self.bst.remove(2)
        self.assertEqual(self.bst.head.left_child.val, 1)

    def test_remove6(self):
        self.bst.add(1)
        self.bst.add(2)
        self.bst.add(3)

        self.bst.remove(2)
        self.assertEqual(self.bst.head.right_child.val, 3)

    def test_remove7(self):
        self.bst.add(4)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)
        self.bst.add(6)
        self.bst.add(5)
        self.bst.add(7)

        self.bst.remove(2)
        self.assertEqual(self.bst.head.left_child.val, 3)

        self.bst.remove(6)
        self.assertEqual(self.bst.head.right_child.val, 7)

    # https://st-lab.tistory.com/300
    def test_remove8(self):
        self.bst.add(23)
        self.bst.add(12)
        self.bst.add(40)
        self.bst.add(7)
        self.bst.add(16)
        self.bst.add(14)
        self.bst.add(15)

        self.bst.remove(12)
        self.assertEqual(self.bst.head.left_child.right_child.left_child.val, 15)

    def test_traverse_pre_order(self):
        self.bst.add(4)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)
        self.bst.add(6)
        self.bst.add(5)
        self.bst.add(7)

        lst = self.bst.traverse_pre_order()
        self.assertEqual(lst, [4, 2, 1, 3, 6, 5, 7])

    def test_traverse_in_order(self):
        self.bst.add(4)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)
        self.bst.add(6)
        self.bst.add(5)
        self.bst.add(7)

        lst = self.bst.traverse_in_order()
        self.assertEqual(lst, [1, 2, 3, 4, 5, 6, 7])

    def test_traverse_post_order(self):
        self.bst.add(4)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(3)
        self.bst.add(6)
        self.bst.add(5)
        self.bst.add(7)

        lst = self.bst.traverse_post_order()
        self.assertEqual(lst, [1, 3, 2, 5, 7, 6, 4])

# 참고
# https://zeddios.tistory.com/492
# https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/
# https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/BinaryTree.py
# https://hongku.tistory.com/160
# https://st-lab.tistory.com/300
