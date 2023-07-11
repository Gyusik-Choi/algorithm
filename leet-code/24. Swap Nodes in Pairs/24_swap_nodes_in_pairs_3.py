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
    # 리턴된 값을 받는 호출 부분은
    # head 의 다음 노드를 가리키던 p 와 head 가 바뀐다
    # p -> head -> 리턴된 값 (단일 노드)
    # 이런 형태로 값을 갖게 되고 여기서 p 를 다시 리턴 하고
    # 이 값을 받는 부분의 p 와 head 도 바뀌고 끝에는
    # p 가 리턴 되면서 함수가 종료된다
    # 재귀의 끝에서 부터 뒤집힌 채로 값이 누적된 p 가 리턴된다
    # 2) head 와 head.next 둘 다 None 이라면
    # None 이 리턴 된다
    # 리턴된 값을 받는 호출 부분은 1) 과 같이 p 와 head 가 바뀐다
    # p -> head -> 리턴된 값 (None)
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
