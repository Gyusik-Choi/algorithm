# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertion_sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 첫번째 풀이와 달리
        # ListNode 의 val 에 None 이 아닌
        # 0을 할당했다
        # 아래 if 문에서 cur.val > head.val 를 할때
        # cur 이 None 인 경우 에러가 나기 때문에
        # 이를 막기 위해 None 대신 0을 할당했다
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next

            # 위에서
            # head 를 head.next 로 이동 하면서
            # head 가 None 이 됐을 수 있기 때문에
            # 조건문에 head 존재 여부를 추가
            #
            # cur.val 이 head.val 보다 크면
            # head.val 보다 더 작은 cur.val 을 찾아야 한다
            # 루트 노드부터 이를 찾을 수 있도록
            # cur 에 루트 노드를 보는 parent 를 할당해서
            # 루트 노드로 이동
            if head and cur.val > head.val:
                cur = parent
        return parent.next


node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)
solution = Solution()
solution.insertion_sort_list(node)
