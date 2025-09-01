package com.example;

public class AddTwoNumbers2_3 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode root = new ListNode();
        ListNode cur = root;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int l1Val = l1 == null ? 0 : l1.val;
            int l2Val = l2 == null ? 0 : l2.val;
            int sum = (l1Val + l2Val + carry) % 10;
            carry = (l1Val + l2Val + carry) / 10;
            cur.next = new ListNode(sum);
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
            cur = cur.next;
        }
        return root.next;
    }
}
