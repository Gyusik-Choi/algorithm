package com.example;

public class PalindromeLinkedList234_7 {
    public boolean isPalindrome(ListNode head) {
        // 1->2->2->1
        // 1->2->3->2->1
        ListNode front = null;
        ListNode cur = head;
        ListNode rear = head;

        // rear != null && next 가 null 이 아니면 이동
        while (rear != null && rear.next != null) {
            rear = rear.next.next;

            ListNode next = cur.next;
            cur.next = front;
            front = cur;
            cur = next;
        }
        // 1->2->3->2->1 처럼
        // 연결 리스트의 길이가 홀수일때
        // cur 이 가운데 3에 위치해 있어서 한칸 더 이동시킨다
        // 그렇게하면 prev 는 왼쪽 2에 있고 cur 는 오른쪽 2에 있게 된다
        if (rear != null) {
            cur = cur.next;
        }

        while (front != null && front.val == cur.val) {
            front = front.next;
            cur = cur.next;
        }
        // while 문의 끝까지 front.val 과 cur.val 이 동일하면
        // front 는 null 이고
        // while 문의 중간에 front.val 과 cur.val 이 다르면
        // while 문이 종료되면서 front 는 null 이 아니다
        return front == null;
    }
}
