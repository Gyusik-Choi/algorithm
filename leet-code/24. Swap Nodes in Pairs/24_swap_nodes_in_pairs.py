class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: ListNode):
    node = head
    # while node.next 조건을 하게 되면
    # AttributeError: 'NoneType' object has no attribute 'next'
    # 에러가 발생한다
    # node 가 None 인 상태면 node 에 next 라는 속성이 없어서 발생한다
    while node and node.next:
        node.val, node.next.val = node.next.val, node.val
        node = node.next.next
    return head


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)
answer = swap_pairs(node1)
print(answer.val)
print(answer.next.val)
print(answer.next.next.val)
print(answer.next.next.next.val)

