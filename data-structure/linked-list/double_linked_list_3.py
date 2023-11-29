from unittest import TestCase


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        # head, tail 을
        # None 이 아닌 빈 노드로 설정하고
        # head 의 next 는 tail 을 보고
        # tail 의 prev 는 head 를 보게 해서
        # head 와 tail 을 연결한다
        # head 와 tail 을 None 으로 할 수도 있지만
        # 타입의 일관성을 지킬 수 있어서 None 대신 빈 노드로 설정한다
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail

    def is_empty(self):
        return self.head.val is None and self.tail.val is None

    def add(self, val):
        # head, tail 이 둘 다 빈 노드인 상태에서
        # 노드가 하나 추가 되면
        # head 는 새 값을 갖는 노드를 보고
        # tail 은 빈 노드를 생성한다
        # head 의 next 는 tail 을 보고
        # tail 의 prev 는 head 를 본다
        # head 와 tail 이 각각 다른 노드를 갖는다
        # head 는 값이 있는 노드, tail 은 빈 노드를 갖는다
        if self.is_empty():
            # 빈 연결 리스트
            # self.head -> None, self.tail -> None
            # 빈 연결 리스트에 노드 하나 추가 (1을 추가한 경우)
            # self.head -> 1, self.tail -> None
            self.head = Node(val)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        # 노드가 1개 이상일 때도
        # tail 은 계속 빈 노드를 바라 보도록 한다
        # tail 과 head 는 계속 각각의 노드를 갖도록 한다
        # 만약에 tail 을 빈 노드가 아니라 값을 갖는 노드로 만들면
        # 노드가 1개만 남을 때 다시 tail 을 빈 노드로 바꿔줘야 한다
        else:
            tail_prev = self.tail.prev
            new_node = Node(val, tail_prev, self.tail)
            tail_prev.next = new_node
            self.tail.prev = new_node

    def add_front(self, val):
        if self.is_empty():
            return self.add(val)

        old_head = self.head
        self.head = Node(val, None, old_head)
        old_head.prev = self.head

    def add_by_idx(self, idx, val):
        if self.is_empty():
            if idx == 0:
                return self.add(val)
            else:
                raise Exception('인덱스를 확인해주세요')

        if idx == 0:
            return self.add_front(val)

        cur = self.head
        i = idx
        while i > 1:
            cur = cur.next
            i -= 1

            if cur is None or cur.val is None:
                raise Exception('인덱스를 확인해주세요')

        new_node = Node(val, cur, cur.next)
        cur.next = new_node
        cur.next.next.prev = new_node

    def remove(self, val):
        if self.is_empty():
            raise Exception('연결리스트가 비었습니다')

        if self.head.val == val:
            # 노드가 1개만 있는 경우
            if self.head.next.val is None:
                self.head = Node(None, None, self.tail)
                self.tail.prev = self.head
            # 노드가 2개 이상 있는 경우
            else:
                self.head = self.head.next
            return

        cur = self.head
        while cur.next.value is not None:
            if cur.val == val:
                prev = cur.prev
                cur.next.prev = prev
                prev.next = cur.next
                break

        raise Exception('해당하는 요소가 없습니다')

    def remove_by_idx(self, idx):
        if self.is_empty():
            raise Exception('연결리스트가 비었습니다')

        if idx == 0:
            return self.remove(self.head.val)

        i = idx
        cur = self.head

        while i > 0:
            i -= 1
            cur = cur.next
            if cur.val is None:
                raise Exception('인덱스를 확인해주세요')

        prev = cur.prev
        next = cur.next
        prev.next = cur.next
        next.prev = prev

    def reverse(self):
        cur = self.head
        prev = Node(None)
        while cur.next:
            # prev.prev 에 cur 을
            cur_node = cur
            next = cur.next
            cur.next = prev
            # prev 를 cur 로 변경하기 전에
            # prev.prev 를 위에서 cur_node 에 담아둔
            # cur 로 설정한다
            prev.prev = cur_node
            prev = cur
            cur = next
        self.tail = self.head.next
        self.head = prev

    def __str__(self):
        nodes = []
        cur = self.head
        while cur.val:
            nodes.append(str(cur.val))
            cur = cur.next
        return ' '.join(nodes)


class TestDoubleLinkedList(TestCase):
    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_is_empty(self):
        self.assertEqual(self.dll.is_empty(), True)

    def test_add(self):
        self.dll.add(1)
        self.dll.add(2)
        self.dll.add(3)

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, 2)
        self.assertEqual(cur.next.next.val, 3)
        self.assertEqual(cur.next.next.next.val, None)

    def test_add_front(self):
        self.dll.add(2)
        self.dll.add(3)
        self.dll.add_front(1)

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, 2)
        self.assertEqual(cur.next.next.val, 3)
        self.assertEqual(cur.next.next.next.val, None)

    def test_add_by_idx(self):
        with self.assertRaises(Exception):
            self.dll.add_by_idx(1, 1)

    def test_add_by_idx2(self):
        self.dll.add(1)
        self.dll.add_by_idx(1, 2)

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, 2)

    def test_add_by_idx3(self):
        self.dll.add(1)
        self.dll.add(3)
        self.dll.add_by_idx(1, 2)

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, 2)
        self.assertEqual(cur.next.next.val, 3)

    def test_remove(self):
        with self.assertRaises(Exception):
            self.dll.remove(1)

    def test_remove2(self):
        self.dll.add(1)
        self.dll.remove(1)
        self.assertEqual(self.dll.head.val, None)
        self.assertEqual(self.dll.tail.val, None)
        self.assertEqual(self.dll.head.next.val, None)
        self.assertEqual(self.dll.tail.prev.val, None)

    def test_remove3(self):
        self.dll.add(1)
        self.dll.add(2)
        self.dll.add(3)

        with self.assertRaises(Exception):
            self.dll.remove(4)

    def test_remove_by_idx(self):
        with self.assertRaises(Exception):
            self.dll.remove_by_idx(0)

    def test_remove_by_idx2(self):
        self.dll.add(1)
        with self.assertRaises(Exception):
            self.dll.remove_by_idx(1)

    def test_remove_by_idx3(self):
        self.dll.add(1)
        self.dll.remove_by_idx(0)
        self.assertEqual(self.dll.head.val, None)
        self.assertEqual(self.dll.tail.val, None)

    def test_remove_by_idx4(self):
        self.dll.add(1)
        self.dll.add(3)
        self.dll.add(2)
        self.dll.remove_by_idx(1)

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, 2)

    def test_remove_by_idx5(self):
        self.dll.add(1)
        self.dll.add(2)
        with self.assertRaises(Exception):
            self.dll.remove_by_idx(2)

    def test_remove_by_idx6(self):
        self.dll.add(1)
        self.dll.add(2)
        self.dll.add(3)
        self.dll.remove_by_idx(2)

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, 2)

    def test_reverse(self):
        self.dll.add(1)
        self.dll.add(2)
        self.dll.add(3)
        self.dll.reverse()

        cur = self.dll.head
        self.assertEqual(cur.val, 3)
        self.assertEqual(cur.next.val, 2)
        self.assertEqual(cur.next.next.val, 1)
        self.assertEqual(cur.next.next.next.val, None)

    def test_reverse2(self):
        self.dll.add(1)
        self.dll.reverse()

        cur = self.dll.head
        self.assertEqual(cur.val, 1)
        self.assertEqual(cur.next.val, None)
