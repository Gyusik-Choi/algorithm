package com.example;

public class AddTwoNumbers2_4 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return add(l1, l2, 0);
    }

    private ListNode add(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null) {
            return carry > 0 ? new ListNode(carry) : null;
        }
        int sum = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val);
        ListNode node = new ListNode((carry + sum) % 10);
        node.next = add(l1 == null ? null : l1.next,  l2 == null ? null : l2.next, (carry + sum) / 10);
        return node;
    }
}
