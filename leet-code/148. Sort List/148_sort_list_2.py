# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sort_list(self, head: ListNode) -> ListNode:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        vals.sort()

        cur = head
        for i in range(len(vals)):
            cur.val = vals[i]
            cur = cur.next

        # cur 이 아니라
        # head 를 리턴해야 한다
        # cur 은
        # 위의 for 문에서
        # 계속 next 를 따라가기 때문에
        # for 문이 끝난 후
        # head 의 맨 끝에 있다
        return head


# -1 5 0 3 4
node = ListNode(-1)
node.next = ListNode(5)
node.next.next = ListNode(0)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)
solution = Solution()
solution.sort_list(node)
