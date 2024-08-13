import java.math.BigInteger;

public class AddTwoNumbers2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode r1 = reverseLinkedList(l1);
        String strNum1 = "";
        while (r1 != null) {
            strNum1 += Integer.toString(r1.val);
            r1 = r1.next;
        }

        ListNode r2 = reverseLinkedList(l2);
        String strNum2 = "";
        while (r2 != null) {
            strNum2 += Integer.toString(r2.val);
            r2 = r2.next;
        }

        BigInteger b1 = new BigInteger(strNum1);
        BigInteger b2 = new BigInteger(strNum2);
        BigInteger bSums = b1.add(b2);
        ListNode b = bigIntegerToListNode(bSums);
        return reverseLinkedList(b);
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

    private ListNode bigIntegerToListNode(BigInteger b) {
        char[] charArr = b.toString().toCharArray();
        ListNode head = new ListNode(Character.getNumericValue(charArr[0]));
        ListNode node = head;
        for (int i = 1; i < charArr.length; i++) {
            node.next = new ListNode(Character.getNumericValue(charArr[i]));
            node = node.next;
        }
        return head;
    }
}
