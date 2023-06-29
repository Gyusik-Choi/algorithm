class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# list1 에 list2 를 합친다
# 기본적으로 list1 과 list2 의 val 중에
# 작은 값을 list1 으로 오게 해서 list1 의 next 에 이어 붙이는 방식이다
# 1.
# list1 이 None 인 경우는 첫번째 if 문을 만족한다
# list2 도 None 이거나 list2 가 None 이 아닌 경우로 나눌 수 있다
# 1-1.
# list2 가 None 인 경우
# list1, list2 의 값을 교환해도 둘 다 None 이다
# 두번째 if 문에는 걸리지 않고 그대로 list1 을 리턴한다
# 탐색을 다 끝내서 둘 다 None 이 된 상태다
# 그동안 list1.next 에 쌓여있던 재귀 호출을
# 하나씩 return 하면서 끝낸다
# 1-2.
# list2 가 None 이 아닌 경우
# list1 과 list2 의 교환이 발생한다
# list2 의 값을 list1 이 갖게 되면서 두번째 if 문을 만족한다
# list1.next 로 재귀 호출이 발생한다
# 2.
# list1 이 None 이 아닌 경우 첫번째 if 문을 만족하지 못한다
# list2 는 None 이거나 None 이 아닌 경우로 나눌 수 있다
# 2-1.
# list2 가 None 인 경우
# 재귀 호출이 발생해도 첫번째 if 문을 만족하지 않아서
# list1 이 None 이 될 때까지 재귀 호출이 계속 일어나고 끝난다
# 2-2.
# list2 가 None 이 아닌 경우
# 재귀 호출이 발생하고 첫번째 if 문은
# list1.val 과 list2.val 의 비교에 따라
# 만족할 수도 있고 만족하지 못할 수도 있다

def merge_two_lists(list1: ListNode, list2: ListNode):
    if not list1 or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1

    if list1:
        list1.next = merge_two_lists(list1.next, list2)

    return list1


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(4)
node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

merge_two_lists(node1, node2)

# 참고
# 파이썬 알고리즘 인터뷰
