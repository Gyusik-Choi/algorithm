class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 연결 리스트 1 -> 2 -> 3 의 경우
# 321 을 구해야 한다
# 역순으로 val 을 나열한 값을 구하기 위해
# val 의 값에 자리수를 곱한다
# 첫번째 연결 리스트는 1의 자리가 돼서 1부터 시작하고
# 하나씩 이동 할수록 10씩 곱한다
def get_reversed_sums(node1, node2):
    node1_number = 0
    node2_number = 0

    node1_digit = 1
    node2_digit = 1

    while node1:
        node1_number += node1.val * node1_digit
        node1 = node1.next
        node1_digit *= 10

    while node2:
        node2_number += node2.val * node2_digit
        node2 = node2.next
        node2_digit *= 10

    return node1_number + node2_number


# get_reversed_sums 에서 역순으로 구한 연결 리스트 간의 합을
# 다시 역순 연결 리스트로 만든다
def get_reversed_linked_list(sums):
    node, prev = None, None

    for idx, num in enumerate(str(sums)):
        node = ListNode(int(num))
        node.next = prev
        prev = node

    return node


def add_two_numbers(l1: ListNode, l2: ListNode):
    return get_reversed_linked_list(get_reversed_sums(l1, l2))


n1 = ListNode(2)
n1.next = ListNode(4)
n1.next.next = ListNode(3)

n2 = ListNode(5)
n2.next = ListNode(6)
n2.next.next = ListNode(4)

add_two_numbers(n1, n2)
