public class AddTwoNumbers2_2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode cur = head;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int sums = 0;

            if (l1 != null) {
                sums += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                sums += l2.val;
                l2 = l2.next;
            }

            int remainder = (carry + sums) % 10;
            carry = (carry + sums) / 10;

            cur.next = new ListNode(remainder);
            cur = cur.next;
        }

        return head.next;
    }
}
