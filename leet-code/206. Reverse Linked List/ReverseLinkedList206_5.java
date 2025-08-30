package com.example;

public class ReverseLinkedList206_5 {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        // cur 에 prev 를 할당하지 않고
        // prev 를 바로 리턴해도 된다
        cur = prev;
        return cur;
    }
}
