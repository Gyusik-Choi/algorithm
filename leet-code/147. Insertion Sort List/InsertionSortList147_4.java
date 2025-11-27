package com.example;

public class InsertionSortList147_4 {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode root = new ListNode(0);
        root.next = head;

        ListNode cur = head;
        ListNode next = head.next;

        while (next != null) {
            // 이미 정렬된 부분은 cur 을 다음 노드로 이동해서 건너뛴다
            // if, else 문 이후에 next = cur.next 에서 보듯이
            // next 가 cur 의 다음 노드에 있도록 한다
            if (cur.val <= next.val) {
                cur = cur.next;
            } else {
                // prev 를 root 로 이동
                ListNode prev = root;
                // prev.next 의 값이 next 의 값보다 작거나 같으면
                // prev 를 다음 노드로 이동
                while (prev.next.val <= next.val) {
                    prev = prev.next;
                }
                // next 의 앞에 있던 cur 의 next 참조를
                // next 의 다음 노드인 next.next 로 변경한다
                // next 가 앞으로 이동하더라도
                // cur 가 계속 next 를 보는게 아니라 next 의 다음 노드를 보게 한다
                cur.next = next.next;
                // next 의 next 참조를
                // prev.next 로 변경한다
                // next 의 next 가 prev 의 다음 노드를 보도록 한다
                next.next = prev.next;
                // prev 의 다음 노드로 next 가 오도록 한다
                // prev 의 다음 노드로 next 가 오고
                // next 의 다음 노드로 기존 prev 의 다음 노드가 오도록 한다
                // 즉, (prev) -> (next) -> (기존 prev.next) 형태가 되도록 한다
                prev.next = next;
            }
            // next 가 cur 의 다음 노드에 있도록 한다
            next = cur.next;
        }

        return root.next;
    }
}
