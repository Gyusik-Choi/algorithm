package com.example;

public class SwapNodesInPairs24_6 {
    public ListNode swapPairs(ListNode head) {
        ListNode root = new ListNode(0);
        root.next = head;
        ListNode prev = root;
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            ListNode nextNext = cur.next.next;
            ListNode next = cur.next;

            prev.next = next;
            next.next = cur;
            cur.next = nextNext;

            prev = cur;
            cur = nextNext;
        }
        return root.next;
    }
}
