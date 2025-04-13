import java.util.Comparator
import java.util.PriorityQueue

class MergeKSortedLists23_2 {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        val pq: PriorityQueue<ListNode> = PriorityQueue<ListNode>(Comparator.comparingInt{ it.`val` })
        for (list: ListNode? in lists) {
            if (list != null) {
                pq.add(list)
            }
        }

        val root: ListNode = ListNode(-1)
        var head: ListNode = root
        while (!pq.isEmpty()) {
            val node: ListNode = pq.poll()
            head.next = node
            head = head.next

            if (node.next != null) {
                pq.add(node.next)
            }
        }

        return root.next
    }
}