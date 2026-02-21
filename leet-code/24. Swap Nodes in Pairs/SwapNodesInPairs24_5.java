package com.example;

public class SwapNodesInPairs24_5 {
    public ListNode swapPairs(ListNode head) {
        ListNode root = new ListNode();
        ListNode prev = root;
        ListNode cur = head;
        root.next = cur;
        while (cur != null && cur.next != null) {
            ListNode next = cur.next;
            ListNode nextNext = next.next;
            prev.next = next;
            next.next = cur;
            cur.next = nextNext;
            prev = cur;
            cur = cur.next;
        }
        return root.next;
    }
}
