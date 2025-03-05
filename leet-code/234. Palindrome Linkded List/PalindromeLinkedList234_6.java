package com.example;

public class PalindromeLinkedList234_6 {

    public boolean isPalindrome(ListNode head) {
        // 런너
        // [1->2->2->1]
        // rev
        // 1->null
        // 2->1->null
        // slow
        // 2->2->1->null
        // 2->1->null
        // [1->2->3->2->1]
        // rev
        // 1->null
        // 2->1->null
        // slow (while 문 아래 if (fast != null) 조건에 의해 slow 는 한칸 앞으로 이동하게 된다)
        // 2->3->2->1->null
        // 3->2->1->null
        ListNode rev = null;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            ListNode temp = rev;
            rev = slow;
            // rev.next = temp;
            // 여기서 rev.next = temp 를 실행하면
            // rev 와 slow 가 동일한 노드를 바라보고 있기 때문에
            // slow 가 null 이 된다
            slow = slow.next;
            fast = fast.next.next;
            rev.next = temp;
        }

        // ListNode 노드 갯수가 홀수인 경우 slow 를 앞으로 한칸 이동
        if (fast != null) {
            slow = slow.next;
        }

        while (rev != null && slow != null) {
            if (rev.val != slow.val) {
                return false;
            }
            rev = rev.next;
            slow = slow.next;
        }
        return true;
    }
}
