package com.example;

public class ReverseLinkedListII92_7 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // left == right -> 바로 반환
        if (left == right) return head;
        ListNode curPrev = null;
        ListNode cur = head;
        for (int i = 1; i < left; i++) {
            curPrev = cur;
            cur = cur.next;
        }
        ListNode curStart = cur;
        ListNode prev = null;
        ListNode next = null;
        for (int i = left; i <= right; i++) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        // 처음부터 끝까지 -> 연결할 앞뒤노드 없음
        if (curPrev == null && next == null) return prev;
        // 처음부터 중간까지 -> 연결할 앞노드 없음
        if (curPrev == null) {
            curStart.next = next;
            return prev;
        }
        // 중간부터 끝까지 -> 연결할 뒤노드 없음
        if (next == null) {
            curPrev.next = prev;
            return head;
        }
        curStart.next = next;
        curPrev.next = prev;
        return head;
    }
}
