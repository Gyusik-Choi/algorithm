package com.example.algorithm;

public class OddEvenLinkedList328_3 {

    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenRef = even;
        while (odd != null && odd.next != null) {
            // 짝수
            if (even != null && even.next == null) {
                odd.next = null;
                break;
            }
            odd.next = odd.next.next;
            even.next = even.next.next;
            odd = odd.next;
            even = even.next;
        }
        odd.next = evenRef;
        return head;
    }
}
