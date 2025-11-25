package com.example;

public class InsertionSortList147_3 {
    public ListNode insertionSortList(ListNode head) {
        ListNode root = new ListNode();
        ListNode prev = root;
        while (head != null) {
            while (prev.next != null && prev.next.val < head.val) {
                prev = prev.next;
            }
            ListNode prevNext = prev.next;
            ListNode headNext = head.next;
            prev.next = head;
            head.next = prevNext;
            head = headNext;

            if (head != null && prev.val > head.val) {
                prev = root;
            }
        }
        return root.next;
    }
}
// 2 4 1 3 5
// p h
//     h
