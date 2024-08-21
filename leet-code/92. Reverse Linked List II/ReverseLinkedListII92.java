public class ReverseLinkedListII92 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head.next == null) {
            return head;
        }

        ListNode root = new ListNode(501);
        root.next = head;

        ListNode node = root;
        for (int i = 1; i < left; i++) {
            node = node.next;
        }
        ListNode leftNode = node;

        for (int i = left; i <= right; i++) {
            node = node.next;
        }
        ListNode rightNode = node.next;
        // 다음 노드와의 연결을 끊는다
        node.next = null;

        ListNode reversedNode = reverse(leftNode.next);
        leftNode.next = reversedNode;
        while (reversedNode.next != null) {
            reversedNode = reversedNode.next;
        }
        reversedNode.next = rightNode;
        return root.next;
    }

    private ListNode reverse(ListNode node) {
        ListNode prev = null;
        while (node != null) {
            ListNode next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return prev;
    }
}
