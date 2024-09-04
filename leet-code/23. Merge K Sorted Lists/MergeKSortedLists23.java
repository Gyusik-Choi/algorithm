import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKSortedLists23 {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.val));
        for (ListNode list : lists) {
            if (list != null) {
                pq.add(list);
            }
        }

        ListNode root = new ListNode(-1);
        ListNode head = root;
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            head.next = node;
            head = head.next;
            if (node.next != null) {
                pq.add(node.next);
            }
        }

        return root.next;
    }
}
