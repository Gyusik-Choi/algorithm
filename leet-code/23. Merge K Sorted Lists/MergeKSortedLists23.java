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
            // node 를 통채로 head.next 에 할당하긴 하지만
            // 다음번 while 문에서 head.next 에 새로 node 를 할당한다
            // 기존 node 의 길이가 2이상이라고 하더라도
            // 기존 node 에서 맨 앞에 있는 노드를 제외하면
            // 나머지 요소들은 다음번 while 문에서 덮어 써진다
            head.next = node;
            head = head.next;
            if (node.next != null) {
                pq.add(node.next);
            }
        }

        return root.next;
    }
}
