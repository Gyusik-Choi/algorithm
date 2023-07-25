class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: ListNode, left: int, right: int):
    if not head or left == right:
        return head

    root = start = ListNode()
    # root 와 head 를 연결
    root.next = head

    # left 만큼 start 이동
    for _ in range(left - 1):
        start = start.next
    # end 는 start 의 다음 노드에 위치
    end = start.next

    for _ in range(right - left):
        temp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = temp

    # root 와 head 를 연결 했는데
    # root.next 를 리턴 하면서 root 는 제외
    return root.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

reverse_between(node, 2, 4)
