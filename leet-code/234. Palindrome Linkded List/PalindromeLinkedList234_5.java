package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class PalindromeLinkedList234_5 {

    public boolean isPalindrome(ListNode head) {
        // 스택 + 런너
        ListNode slow = head;
        ListNode fast = head;
        Deque<Integer> stack = new ArrayDeque<>();
        while (fast != null && fast.next != null) {
            stack.push(slow.val);
            slow = slow.next;
            fast = fast.next.next;
        }

        // ListNode 노드 갯수가 홀수인 경우 slow 를 앞으로 한칸 이동
        if (fast != null) {
            slow = slow.next;
        }

        while (slow != null) {
            if (slow.val != stack.pop()) {
                return false;
            }
            slow = slow.next;
        }
        return true;
    }
    // 1 2 2 1
    //
    // 1->2
    // 1->2->2
    //
    // 1->2->2
    // 1->2->2->1->null
    //
    // 1 2 3 2 1
    //
    // 1->2
    // 1->2->3
    //
    // 1->2->3
    // 1->2->3->2->1
    // fast.next == null -> 홀수
}
