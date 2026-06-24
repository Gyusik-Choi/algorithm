package com.example;

public class InsertionSortList147_5 {
    public ListNode insertionSortList(ListNode head) {
        ListNode sortedNode = new ListNode();
        while (head != null) {
            ListNode cur = sortedNode;
            while (cur.next != null && cur.next.val < head.val) {
                cur = cur.next;
            }
            ListNode temp = head;
            head = head.next;
            temp.next = null;
            ListNode curNext = cur.next;
            cur.next = temp;
            cur.next.next = curNext;
        }
        return sortedNode.next;
    }
}
