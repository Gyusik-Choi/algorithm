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

        // prev 는 역순으로 뒤집은 연결 리스트를 가리키게 된다
        // node 는 역순으로 뒤집은 연결 리스트의 이후 노드를 가리키게 된다
        ListNode prev = null;
        for (int i = left; i <= right; i++) {
           ListNode next = node.next;
           node.next = prev;
           prev = node;
           node = next;
        }

        // prev 가 null 이 아니면
        // leftNode 와 prev 를 연결하고 prev 와 node 를 연결한다
        if (prev != null) {
            leftNode.next = prev;
            while (prev.next != null) {
                prev = prev.next;
            }
            prev.next = node;
        // prev 가 null 이면
        // leftNode 와 node 를 연결한다
        } else {
            leftNode.next = node;
        }

        return root.next;
    }
}
