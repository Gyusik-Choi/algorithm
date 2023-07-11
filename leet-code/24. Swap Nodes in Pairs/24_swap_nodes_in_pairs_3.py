class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: ListNode):
    # head 와 head.next 가 None 이 될 때까지
    # swap_pairs 를 재귀 호출한다
    # if 문을 만족하지 않을때 두가지 경우가 있다
    # 1) head 가 None 이 아니고 head.next 가 None 이라면
    # head 가 가리키는 단일 노드가 리턴 된다
    # p 에 head 의 next 가 가리키는 노드가 대입 되어 있고
    # 앞서 리턴된 노드는 head 의 next 속성의 값으로 대입 된다
    #
    if head and head.next:
        p = head.next
        head.next = swap_pairs(p.next)
        p.next = head
        return p
    return head


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
answer = swap_pairs(node)

print(answer.val)
print(answer.next.val)
print(answer.next.next.val)
print(answer.next.next.next.val)
