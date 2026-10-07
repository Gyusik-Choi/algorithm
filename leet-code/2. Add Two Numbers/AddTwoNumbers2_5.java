package com.example;

public class AddTwoNumbers2_5 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode answer = new ListNode(0);
        add(l1, l2, answer, 0);
        return answer.next;
    }

    private void add(ListNode l1, ListNode l2, ListNode addNode, int carryIn) {
        if (l1 == null && l2 == null) {
            if (carryIn > 0) {
                addNode.next = new ListNode(carryIn);
            }
            return;
        }
        if (l1 == null) {
            int sum = (l2.val + carryIn) % 10;
            int carryOut = (l2.val + carryIn) / 10;
            addNode.next = new ListNode(sum);
            add(null, l2.next, addNode.next, carryOut);
            return;
        }
        if (l2 == null) {
            int sum = (l1.val + carryIn) % 10;
            int carryOut = (l1.val + carryIn) / 10;
            addNode.next = new ListNode(sum);
            add(l1.next, null, addNode.next, carryOut);
            return;
        }
        int sum = (l1.val + l2.val + carryIn) % 10;
        int carryOut = (l1.val + l2.val + carryIn) / 10;
        addNode.next = new ListNode(sum);
        add(l1.next, l2.next, addNode.next, carryOut);
    }
}
