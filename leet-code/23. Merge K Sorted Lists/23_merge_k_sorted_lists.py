import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_k_sorted_lists(self, lists: list[ListNode]) -> list[ListNode]:
        head = ListNode()
        cur = head
        heap = []

        for idx, lst in enumerate(lists):
            if not lst:
                continue

            heapq.heappush(heap, (lst.val, idx, lst))

        while heap:
            value, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if cur.next:
                heapq.heappush(heap, (cur.next.val, i, cur.next))

        return head.next
