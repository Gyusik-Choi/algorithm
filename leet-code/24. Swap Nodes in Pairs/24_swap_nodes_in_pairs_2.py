class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: ListNode):
    # root 와 prev 가 같은 노드를 가리킨다
    root = ListNode(None)
    prev = root
    # prev 의 next 속성을 head 로 설정
    # (prev 와 head 가 next 속성으로 연결됐다)
    prev.next = head

    while head and head.next:
        # 선언 부분의 next 는 속성명
        # 대입 부분의 next 는 노드 (next 속성이 가리키는 노드)
        #
        # head 의 next 속성이 가리키는 노드를 temp 에 대입
        temp = head.next
        # head 의 next 속성을 변경
        head.next = temp.next
        # temp 의 next 속성을 head 로 설정
        temp.next = head

        # prev 의 next 속성을 temp 로 설정
        prev.next = temp

        # head 자체를 head.next 로 변경
        head = head.next
        # prev 자체를 prev.next.next 로 변경
        prev = prev.next.next
    # prev 는 prev.next.next 로 이동 하면서 가리키는 노드가 변했지만
    # root 는 변하지 않았다
    return root.next


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)
answer = swap_pairs(node1)
print(answer.val)
print(answer.next.val)
print(answer.next.next.val)
print(answer.next.next.next.val)
