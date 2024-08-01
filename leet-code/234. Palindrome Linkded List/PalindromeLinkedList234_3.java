/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

import java.util.*;


public class PalindromeLinkedList234_3 {
    public boolean isPalindrome(ListNode head) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        ListNode cur = head;
        while (cur != null) {
            deque.add(cur.val);
            cur = cur.next;
        }
        while (!deque.isEmpty() && deque.size() > 1) {
            if (!Objects.equals(deque.pollFirst(), deque.pollLast())) {
                return false;
            }
        }
        return true;
    }
}
