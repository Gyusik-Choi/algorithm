package com.example;

public class ReverseLinkedList206_6 {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode next = head.next;
        head.next = null;
        // 마지막으로 리턴받은 (if 문)
        // head 의 참조를 받게되고
        // 이를 그대로 계속 리턴한다
        // 마지막 노드에 대한 참조를 유지할 수 있다
        // 1->2->3->4->5
        // 위와 같은 노드가 주어진다고 가정할때
        // 5에 대한 참조를 reverse 가 갖게되고
        // reverseList 메소드 내부에서는
        // 5->4->3->2->1 로 변경이 발생한다
        ListNode reverse = reverseList(next);
        next.next = head;
        return reverse;
    }
}
