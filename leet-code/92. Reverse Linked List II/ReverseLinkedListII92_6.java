package com.example;

public class ReverseLinkedListII92_6 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode prev = null;
        ListNode cur = head;
        for (int i = 0; i < left - 1; i++) {
            prev = cur;
            cur = cur.next;
        }
        ListNode curRef = cur;
        ListNode front = null;
        for (int i = 0; i < right - left + 1; i++) {
            ListNode rear = cur.next;
            cur.next = front;
            front = cur;
            cur = rear;
        }
        // head 부터 뒤집는 경우
        // (첫번째 for 문이 loop 를 돌지 못하고 종료돼서 prev 가 갱신되지 못하고 null 인 상태로 남음)
        if (prev != null) {
            prev.next = front;
        }
        curRef.next = cur;
        return prev == null ? front : head;
    }
}
