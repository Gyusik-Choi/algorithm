# 연결리스트는 데이터의 삽입 및 삭제에 용이하지만
# 배열과 달리 인덱스 개념이 없기 때문에 탐색은 배열의 길이 만큼(O(n)) 수행해야 한다.

# 단순 연결리스트 구조는 하나씩 줄을 매달아 세우듯이 첫번째가 두번째를 가리키고, 두번째가 세번째를 가리키면서 이어진다.
# 맨 끝의 요소를 찾으려면 처음부터 끝까지 가야한다.
# 단순 연결리스트에서 탐색의 시간을 조금이나마 높이고자 맨 마지막에 tail 을 사용해서 맨 마지막 요소를 가리키도록 한다.
# 이중 연결리스트가 아니기 때문에 tail 은 tail 앞의 요소를 가리키지 않고 단지 tail 이 어떤 요소인지 가리키고만 있는다.
# 맨 마지막 요소를 찾을 때 빠르게 찾을 수 있다.


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        # size 변수를 통해 여기서는 활용하지 않았지만 is_empty() 를 판단할 수도 있고
        # insert 메소드를 사용할 때 잘못된 인덱스 요청인지 판단할 수 있다.
        # 예를 들어, 연결리스트의 size 가 3인데 인덱스 5에 넣을 수 없다.
        self.size = 0

    def is_empty(self):
        if self.head.val is None:
            return True
        return False

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head

        # append 는 맨 뒤에 요소를 삽입하므로 따로 탐색과정 없이 바로 tail 에서 추가하면 된다.
        # 단 요소가 1개 일때 tail 에 삽입하면 head 와의 관계가 끊긴다.
        # 이때는 head 의 next 로 넣고 tail 이 이를 가리키도록 한다.
        else:
            # 요소 1개
            if self.head == self.tail:
                self.head.next = Node(item)
                self.tail = self.head.next
            # 요소 여러개
            else:
                cur = self.tail
                cur.next = Node(item)
                # self.tail 이 새로운 마지막 요소를 가리키도록 한다.
                self.tail = cur.next

        self.size += 1

    def append_first(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            cur = self.head
            self.head = Node(item)
            self.head.next = cur
        self.size += 1

    def insert(self, idx, item):
        if self.size < idx:
            print("Wring Index")
            return

        # 맨 앞에 insert
        if idx == 0:
            if self.is_empty():
                self.head = Node(item)
                self.tail = self.head
            else:
                cur = self.head
                self.head = Node(item)
                self.head.next = cur
        # 맨 뒤에 insert
        elif idx == self.size:
            # 요소 1개
            if self.head == self.tail:
                self.head.next = Node(item)
                self.tail = self.head.next
            # 요소 여러개
            else:
                cur = self.tail
                cur.next = Node(item)
                self.tail = cur.next
        # 맨 앞도 맨 뒤도 아닌 어딘가
        else:
            i = idx
            cur = self.head
            while i > 1:
                cur = cur.next
                i -= 1
            original_next = cur.next
            cur.next = Node(item)
            cur.next.next = original_next

        self.size += 1

    def remove_last_item(self):
        if self.is_empty():
            print("Nothing to remove")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = self.head
        else:
            # 그냥 tail 을 지워버리면 안 된다.
            # tail 앞의 요소의 next 가 tail 을 가리키지 않고 None 이 되야 한다.
            # 그리고 tail 은 None 이 된 기존 요소가 아니라 이 앞의 요소를 가리켜야 한다.
            cur = self.head
            # 아래의 while 문의 조건을 cur.next.next 가 아니라 cur.next 로 하게 되면 cur 이 맨 마지막 노드를 가리키게 된다
            # 그러면 맨 마지막 노드를 지우기 어렵다. 맨 마지막 노드의 앞 노드에 cur 가 오도록 하면
            # 이 노드의 next 를 None 으로 해서 맨 마지막 노드를 지울 수 있다.
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
            self.tail = cur
        self.size -= 1

    def remove_by_item(self, item):
        if self.is_empty():
            print("Nothing to remove")
            return

        # 맨 앞의 요소 삭제
        if self.head.val == item:
            # 요소가 1개
            if self.head == self.tail:
                self.head = self.head.next
                self.tail = self.head.next
            # 요소가 여러개
            else:
                self.head = self.head.next
        else:
            cur = self.head
            # 지울 대상 요소의 앞 요소에 cur 가 오도록 한다
            while cur.next.val == item:
                cur = cur.next
            # 지울 대상의 next 요소가 지울 대상 앞의 요소인 cur 의 next 로 연결되게 한다
            # 지울 대상은 자연스럽게 연결고리에서 빠진다
            # 단 지울 대상이 tail 이면 그냥 지우면 안 되고 tail 이 지울 대상의 앞 요소를 가리키도록 해야 한다
            if cur.next == self.tail:
                next_node = cur.next.next
                cur.next = next_node
                self.tail = cur.next
            else:
                next_node = cur.next.next
                cur.next = next_node
        self.size -= 1

    def remove_by_index(self, idx):
        if self.is_empty():
            print("Nothing to remove")
            return

        if idx == 0:
            # 요소가 1개
            if self.head == self.tail:
                self.head = self.head.next
                self.tail = self.head.next
            else:
                self.head = self.head.next
        else:
            cur = self.head
            i = idx
            while i > 1:
                cur = cur.next
                i -= 1
            if cur.next == self.tail:
                next_node = cur.next.next
                cur.next = next_node
                self.tail = cur.next
            else:
                next_node = cur.next.next
                cur.next = next_node
        self.size -= 1

    def reverse(self):
        cur = self.head
        self.tail = cur
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def __str__(self):
        lst = "["
        cur = self.head
        while cur:
            lst += str(cur.val) + ", "
            cur = cur.next
        lst = lst.rstrip(", ")
        lst += "]"
        return lst


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.reverse()
ll.remove_by_index(2)
ll.print_list()
print(ll)

# 참고
# https://namu.wiki/w/%EC%97%B0%EA%B2%B0%20%EB%A6%AC%EC%8A%A4%ED%8A%B8
# # https://underflow101.tistory.com/3?category=826162
