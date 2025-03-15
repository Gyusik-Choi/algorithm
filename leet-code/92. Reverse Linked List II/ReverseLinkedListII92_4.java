package com.example;

public class ReverseLinkedListII92_4 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode root = new ListNode(0);
        root.next = head;
        ListNode prevRef = root;
        ListNode cur = head;

        for (int i = 0; i < left - 1; i++) {
            prevRef = cur;
            cur = cur.next;
        }

        ListNode curRef = cur;
        ListNode prev = null;
        for (int i = 0; i < right - left + 1; i++) {
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
