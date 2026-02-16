package com.example;

public class ReverseLinkedList206_7 {
    public ListNode reverseList(ListNode head) {
        ListNode reversedHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = reversedHead;
            reversedHead = head;
            head = next;
        }
        return reversedHead;
    }
}
