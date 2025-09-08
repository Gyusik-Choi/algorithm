package com.example;

public class ReverseLinkedListII92_5 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode root = new ListNode(0);
        root.next = head;

        ListNode prevRef = root;
        ListNode curRef = head;
        for (int i = 0; i < left - 1; ++i) {
            prevRef = curRef;
            curRef = curRef.next;
        }

        ListNode prev = prevRef;
        ListNode cur = curRef;
        for (int i = 0; i <= right - left; i++) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        prevRef.next = prev;
        curRef.next = cur;
        return root.next;
    }
}
