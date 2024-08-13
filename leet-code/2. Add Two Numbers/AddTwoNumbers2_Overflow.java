public class AddTwoNumbers2_Overflow {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int num1 = 0;
        int digit1 = 1;
        while (l1 != null) {
            num1 += l1.val * digit1;
            digit1 *= 10;
            l1 = l1.next;
        }

        int num2 = 0;
        int digit2 = 1;
        while (l2 != null) {
            num2 += l2.val * digit2;
            digit2 *= 10;
            l2 = l2.next;
        }

        int sums = num1 + num2;
        char[] charSums = Integer.toString(sums).toCharArray();

        ListNode answer = new ListNode(Character.getNumericValue(charSums[0]));
        ListNode node = answer;
        for (int i = 1; i < charSums.length; i++) {
            node.next = new ListNode(Character.getNumericValue(charSums[i]));
            node = node.next;
        }

        return reverseLinkedList(answer);
    }

    private ListNode reverseLinkedList(ListNode node) {
        return reverse(node, null);
    }

    private ListNode reverse(ListNode cur, ListNode prev) {
        if (cur == null) {
            return prev;
        }

        ListNode next = cur.next;
        cur.next = prev;
        return reverse(next, cur);
    }
}
