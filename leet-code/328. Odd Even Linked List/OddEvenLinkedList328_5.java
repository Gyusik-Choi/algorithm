package com.example;

public class OddEvenLinkedList328_5 {
    public ListNode oddEvenList(ListNode head) {
        ListNode root = new ListNode(0);
        root.next = head;
        ListNode odd = head;
        ListNode even = odd != null ? odd.next : null;
        ListNode evenRef = even;
        while (odd != null && odd.next != null && odd.next.next != null) {
            odd.next = odd.next.next;
            even.next = even.next.next;
            odd = odd.next;
            even = even.next;
        }
        if (odd != null) {
            odd.next = evenRef;
        }
        return root.next;
    }
}
