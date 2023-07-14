class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: ListNode):
    if head is None:
        return None

    # head 를 변경 하지 않으면서
    # odd 의 시작 부분을 head 가 유지
    odd = head
    even = head.next
    # even 의 시작 부분을 even_head 가 유지
    even_head = head.next

    while even and even.next:
        # odd 의 next 속성과 even 의 next 속성을 변경 한다
        # (odd 의 다음 노드, even 의 다음 노드를 변경 하는게 아니다)
        odd.next, even.next = odd.next.next, even.next.next
        # odd 에 odd 의 다음 노드를 대입하고
        # even 에 even 의 다음 노드를 대입한다
        # (위에서 변경 시킨 next 속성이 보는 노드를 보게 된다)
        odd, even = odd.next, even.next

    # odd 의 next 속성에 even_head 를 대입
    odd.next = even_head
    return head


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

answer = odd_even_list(node)

# 참고
# 파이썬 알고리즘 인터뷰
