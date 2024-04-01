from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertion_sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            cur = parent

        return cur.next


node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)
solution = Solution()
solution.insertion_sort_list(node)
