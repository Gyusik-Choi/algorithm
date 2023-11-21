from unittest import TestCase


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None)

    def is_empty(self):
        return self.head.val is None

    def add(self, val):
        if self.head.val is None:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)

    def add_front(self, val):
        if self.head.val is None:
            self.head = Node(val)
        else:
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head

    def add_by_idx(self, idx, val):
        if idx == 0:
            return self.add_front(val)

        if self.head.val is None:
            raise Exception('인덱스를 확인 해주세요')

        cur = self.head
        i = idx
        while i > 1:
            cur = cur.next
            if cur is None:
                raise Exception('인덱스를 확인 해주세요')
            i -= 1

        old_next = cur.next
        cur.next = Node(val)
        cur.next.next = old_next

    # 해당하는 노드가 없으면 삭제되지 않는다
    def remove(self, val):
        if self.head.val == val:
            if self.head.next is None:
                self.head = Node(None)
            else:
                self.head = self.head.next
        else:
            cur = self.head
            while cur.next:
                if cur.next.val == val:
                    cur.next = cur.next.next
                    return
                else:
                    cur = cur.next
            raise Exception('값을 확인 해주세요')

    def remove_by_idx(self, idx):
        if self.head.val is None:
            return

        if idx == 0:
            return self.remove(self.head.val)

        cur = self.head
        i = idx
        while i > 1:
            if cur.next is None:
                # break 이후 아래의 if 문을 충족하지 못해서
                # Exception 발생한다
                break
            cur = cur.next
            i -= 1

        if not cur.next:
            raise Exception('인덱스를 확인 해주세요')
        cur.next = cur.next.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            rear = cur.next
            cur.next = prev
            prev = cur
            cur = rear
        # cur 은 None 이 됐다
        # self.head 가 뒤집힌 연결 리스트의
        # 시작 노드를 바라볼 수 있도록 재설정
        self.head = prev

    def __str__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(str(cur.val))
            cur = cur.next
        return ' '.join(nodes)


class TestSinglyLinkedList(TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_is_empty(self):
        self.assertEqual(self.linked_list.is_empty(), True)

    def test_is_empty2(self):
        self.linked_list.add(1)
        self.assertEqual(self.linked_list.is_empty(), False)

    def test_add(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.assertEqual(self.linked_list.head.val, 1)
        self.assertEqual(self.linked_list.head.next.val, 2)
        self.assertEqual(self.linked_list.head.next.next.val, 3)

    def test_add_first(self):
        self.linked_list.add_front(1)
        self.assertEqual(self.linked_list.head.val, 1)

    def test_add_first2(self):
        self.linked_list.add(2)
        self.linked_list.add_front(1)
        self.assertEqual(self.linked_list.head.val, 1)

    def test_add_by_idx(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add_by_idx(3, 4)
        self.assertEqual(self.linked_list.head.next.next.next.val, 4)

    # https://www.geeksforgeeks.org/test-if-a-function-throws-an-exception-in-python/
    def test_add_by_idx2(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        with self.assertRaises(Exception):
            self.linked_list.add_by_idx(4, 4)

    def test_remove(self):
        self.linked_list.add(1)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list.head.val, None)

    def test_remove2(self):
        self.linked_list.add(1)
        with self.assertRaises(Exception):
            self.linked_list.remove(2)

    def test_remove3(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list.head.val, 1)
        self.assertEqual(self.linked_list.head.next.val, 3)

    def test_remove4(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove(3)
        self.assertEqual(self.linked_list.head.val, 1)
        self.assertEqual(self.linked_list.head.next.val, 2)

    def test_remove_by_idx(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove_by_idx(0)
        self.assertEqual(self.linked_list.head.val, 2)
        self.assertEqual(self.linked_list.head.next.val, 3)

    def test_remove_by_idx2(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove_by_idx(1)
        self.assertEqual(self.linked_list.head.val, 1)
        self.assertEqual(self.linked_list.head.next.val, 3)

    def test_remove_by_idx3(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove_by_idx(2)
        self.assertEqual(self.linked_list.head.val, 1)
        self.assertEqual(self.linked_list.head.next.val, 2)

    def test_remove_by_idx4(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        with self.assertRaises(Exception):
            self.linked_list.remove_by_idx(3)

    def test_reverse(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add(4)
        self.linked_list.add(5)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.head.val, 5)
        self.assertEqual(self.linked_list.head.next.val, 4)
        self.assertEqual(self.linked_list.head.next.next.val, 3)
        self.assertEqual(self.linked_list.head.next.next.next.val, 2)
        self.assertEqual(self.linked_list.head.next.next.next.next.val, 1)
