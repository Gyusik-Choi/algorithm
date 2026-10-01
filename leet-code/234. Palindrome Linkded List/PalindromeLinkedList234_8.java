package com.example;

public class PalindromeLinkedList234_8 {
    public boolean isPalindrome(ListNode head) {
        if (head.next == null) {
            return true;
        }
        ListNode left = null;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;

            ListNode next = slow.next;
            slow.next = left;
            left = slow;
            slow = next;
        }

        ListNode right = slow;
        // head 의 길이가 홀수면 right 한 칸 더 이동
        if (fast != null) {
            right = right.next;
        }
        while (left != null && right != null) {
            if (left.val != right.val) {
                return false;
            }
            left = left.next;
            right = right.next;
        }
        return true;
    }
}
