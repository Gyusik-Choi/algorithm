class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 입력으로 주어지는 노드는 단일 연결 리스트
def is_palindrome(head: ListNode):
    two_step = head
    one_step = head
    rev = None

    while two_step and two_step.next:
        two_step = two_step.next.next
        rev, rev.next, one_step = one_step, rev, one_step.next

    if two_step:
        one_step = one_step.next

    while one_step and one_step.val == rev.val:
        one_step, rev = one_step.next, rev.next

    return not rev


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
print(is_palindrome(node))

# 참고
# 파이썬 알고리즘 인터뷰
