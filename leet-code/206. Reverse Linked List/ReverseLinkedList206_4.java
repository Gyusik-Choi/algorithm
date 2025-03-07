package com.example;

public class ReverseLinkedList206_4 {

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode temp = prev;
            prev = cur;
            cur = cur.next;
            prev.next = temp;
        }
        return prev;
    }
}