public class ReverseLinkedList206_2 {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode next = reverseList(head.next);
        ListNode prev = new ListNode(head.val);
        ListNode cur = next;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = prev;
        return next;
    }
}
