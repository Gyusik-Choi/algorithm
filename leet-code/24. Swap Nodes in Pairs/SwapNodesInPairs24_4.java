package com.example;

public class SwapNodesInPairs24_4 {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode farNext = head.next.next;
        ListNode next = head.next;
        next.next = head;
        head.next = swapPairs(farNext);
        return next;
    }
}
