public class ReverseLinkedList206_3 {
    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }

    private ListNode reverse(ListNode cur, ListNode prev) {
        if (cur == null) {
            return prev;
        }

        ListNode next = cur.next;
        cur.next = prev;
        return reverse(next, cur);
    }
}
