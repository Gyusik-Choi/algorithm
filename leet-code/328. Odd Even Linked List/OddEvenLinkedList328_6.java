package com.example;

public class OddEvenLinkedList328_6 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode odd = head;
        ListNode oddRef = odd;
        ListNode even = head.next;
        ListNode evenRef = even;
        while (odd.next != null && odd.next.next != null) {
            odd.next = odd.next.next;
            odd = odd.next;
            even.next = even.next.next;
            even = even.next;
        }
        odd.next = evenRef;
        return oddRef;
    }
    // 1->2->3
    // 1->2->3->4
}
