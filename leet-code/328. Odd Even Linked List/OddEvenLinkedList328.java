public class OddEvenLinkedList328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode[] nodes = separate(head);
        while (nodes[0].next != null) {
            nodes[0] = nodes[0].next;
        }
        nodes[0].next = nodes[1];
        return head;
    }

    private ListNode[] separate(ListNode node) {
        if (node == null || node.next == null) {
            return new ListNode[]{node, null};
        }

        ListNode[] nodes = separate(node.next.next);
        ListNode next = node.next;
        node.next = nodes[0];
        next.next = nodes[1];
        return new ListNode[]{node, next};
    }
}
