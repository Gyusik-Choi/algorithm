# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 두 정렬 리스트 병합
    def __merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            # __merge_two_lists 재귀 호출의 결과가
            # li.next 에 할당 되면서
            # 노드 간의 연결이 끊기지 않는다
            l1.next = self.__merge_two_lists(l1.next, l2)

        return l1 or l2

    def sort_list(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sort_list(head)
        l2 = self.sort_list(slow)

        return self.__merge_two_lists(l1, l2)


# -1 5 0 3 4
node = ListNode(-1)
node.next = ListNode(5)
node.next.next = ListNode(0)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)
solution = Solution()
solution.sort_list(node)
