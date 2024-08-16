public class SwapNodesInPairs24_2 {
    public ListNode swapPairs(ListNode head) {
        // 임시 노드
        ListNode node = new ListNode();
        ListNode root = node;
        // 임시 노드의 next 에 head 를 연결
        node.next = head;
        while (node.next != null && node.next.next != null) {
            ListNode a = node.next;
            ListNode b = node.next.next;
            a.next = b.next;
            node.next = b;
            node.next.next = a;

            node = node.next.next;
        }
        // 임시 노드의 다음 노드를 리턴
        return root.next;
    }
}
