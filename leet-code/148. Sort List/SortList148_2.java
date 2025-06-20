package com.example;

public class SortList148_2 {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode half = null;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            half = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        // half 를 통해 head 의 연결을 끊는다
        half.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(slow);
        return mergeList(left, right);
    }

    private ListNode mergeList(ListNode l1, ListNode l2) {
        // l1 이 null 이면 l2 를 리턴해서
        // l1.next 에 l2 가 할당될 수 있도록 한다
        if (l1 == null) {
            return l2;
        }

        // l2 가 null 이면 l1 을 리턴해서
        // l1.next 에 l1 이 할당될 수 있도록 한다
        if (l2 == null) {
            return l1;
        }

        // l1.val 이 l2.val 보다 크면
        // l1 과 l2 를 교환한다
        // l1 은 기존의 l2 를 가리키고 있고
        // l1 의 next 가 될 노드를
        // l1.next 와 l2 를 재귀로 비교해서 구한다
        if (l1.val > l2.val) {
            ListNode temp = l1;
            l1 = l2;
            l2 = temp;
        }

        l1.next = mergeList(l1.next, l2);
        return l1;
    }
}
