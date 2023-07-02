class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1 -> 2 -> 3 -> 4 -> 5 -> None
def reverse_list(head):
    rev = None
    while head:
        rev, rev.next, head = head, rev, head.next
    return rev


# 연결 리스트 생성 함수
def create_node(node, n, limit):
    if n > limit:
        return

    node.next = ListNode(n)
    create_node(node.next, n + 1, limit)
    return node


node1 = create_node(ListNode(1), 2, 5)
# print(node1.next.next.next.next.val)
answer = reverse_list(node1)
print(answer.next.next.next.next.val)
