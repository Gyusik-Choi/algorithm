public class ReverseLinkedListII92_3 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head.next == null) {
            return head;
        }

        ListNode root = new ListNode(501);
        root.next = head;
        ListNode start = root;
        for (int i = 0; i < left - 1; i++) {
            start = start.next;
        }

        ListNode end = start.next;
        for (int i = 0; i < right - left; i++) {
            ListNode temp = start.next;
            start.next = end.next;
            end.next = end.next.next;
            start.next.next = temp;
        }

        return root.next;
    }
}
