class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1 -> 2 -> 3 -> 4 -> 5 -> None
def reverse_list(head):
    def reverse(cur, prev):
        if not cur:
            return prev

        next, cur.next = cur.next, prev
        return reverse(next, cur)

    return reverse(head, None)


# 연결 리스트 생성 함수
def create_node(node, n, limit):
    if n > limit:
        return

    node.next = ListNode(n)
    create_node(node.next, n + 1, limit)
    return node


node1 = create_node(ListNode(1), 2, 5)
answer = reverse_list(node1)
print(answer.val)
