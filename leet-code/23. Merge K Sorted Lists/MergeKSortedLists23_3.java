package com.example;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKSortedLists23_3 {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode root = new ListNode();
        ListNode cur = root;
        PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.val));
        Arrays.stream(lists).forEach(item -> { if (item != null) pq.add(item); });
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
