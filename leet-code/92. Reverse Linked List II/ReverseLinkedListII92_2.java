public class ReverseLinkedListII92_2 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head.next == null) {
            return head;
        }

        ListNode root = new ListNode(501);
        root.next = head;
        ListNode leftNode = root;
        ListNode node = head;
        for (int i = 1; i < left; i++) {
            leftNode = node;
            node = node.next;
        }

        ListNode prev = null;
        for (int i = left; i <= right; i++) {
           ListNode next = node.next;
           node.next = prev;
           prev = node;
           node = next;
        }

        if (prev != null) {
            leftNode.next = prev;
            while (prev.next != null) {
                prev = prev.next;
            }
            prev.next = node;
        } else {
            leftNode.next = node;
        }

        return root.next;
    }
}
