package com.example;

public class SwapNodesInPairs24_3 {
    public ListNode swapPairs(ListNode head) {
        ListNode root = new ListNode(0);
        root.next = head;
        ListNode prev = root;
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            prev.next = cur.next;
            ListNode next = cur.next;
            cur.next = next.next;
            next.next = cur;

            prev = cur;
            cur = cur.next;
        }
        return root.next;
    }
}
