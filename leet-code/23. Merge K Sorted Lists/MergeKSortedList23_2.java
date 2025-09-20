package com.example;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKSortedList23_2 {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(n -> n.val));
        for (ListNode node : lists) {
            if (node != null) {
                pq.add(node);
            }
        }
        ListNode root = new ListNode(-1);
        ListNode cur = root;
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            ListNode next = node.next;
            node.next = null;
            cur.next = node;
            cur = cur.next;
            if (next != null) {
                pq.add(next);
            }
        }
        return root.next;
    }
}
