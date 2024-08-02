public class PalindromeLinkedList234_4 {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // 홀수
        if (fast != null) {
            slow = slow.next;
        }

        ListNode prev = null;

        while (slow != null) {
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }

        // slow 에 prev 를 할당하지 않으면
        // 아래 while 문에서 slow 대신 prev 를 사용하는 방법도 있다
        slow = prev;

        while (slow != null) {
            if (head.val != slow.val) {
                return false;
            }
            head = head.next;
            slow = slow.next;
        }

        return true;
    }
}
