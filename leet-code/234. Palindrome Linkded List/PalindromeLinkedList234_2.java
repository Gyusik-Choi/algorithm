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

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class PalindromeLinkedList234_2 {
    public boolean isPalindrome(ListNode head) {
        List<Integer> nums = new ArrayList<>();
        while (head != null) {
            nums.add(head.val);
            head = head.next;
        }
        List<Integer> reversedNums = new ArrayList<>(nums);
        Collections.reverse(reversedNums);
        return nums.equals(reversedNums);
    }
}
