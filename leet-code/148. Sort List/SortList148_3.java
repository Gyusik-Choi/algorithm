package com.example;

public class SortList148_3 {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode prev = null;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        ListNode root = new ListNode();
        ListNode cur = root;
        ListNode left = sortList(head);
        ListNode right = sortList(slow);
        ListNode l = left;
        ListNode r = right;
        while (l != null && r != null) {
            if (l.val < r.val) {
                cur.next = l;
                l = l.next;
            } else {
                cur.next = r;
                r = r.next;
            }
            cur.next.next = null;
            cur = cur.next;
        }
        if (cur != null && l != null) {
            cur.next = l;
        }
        while (cur != null && cur.next != null) {
            cur = cur.next;
        }
        if (cur != null && r != null) {
            cur.next = r;
        }
        return root.next;
    }
}
