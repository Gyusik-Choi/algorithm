package com.example;

public class SortList148 {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        // half 는 slow 가 head 와 연결되지 않도록 한다
        // (while 문 종료후에 half.next 에 null 할당해서 연결을 끊음)
        // slow 는 연결리스트 가운데 정점을 가리키는 노드
        // fast 는 두칸씩 이동하면서 연결리스트의 끝까지 이동한다
        ListNode half = null, slow = head, fast = head;
        // while (fast.next.next != null)
        // 위의 조건은 연결리스트의 길이가 2이하인 경우 사용할 수 없다
        // 반면에 아래의 조건은 연결리스트의 길이가 2일때
        // fast 가 이동할 수 있어서 half 와 slow 를 갱신할 수 있다
        while (fast != null && fast.next != null) {
            half = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        half.next = null;

        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);
        return mergeList(l1, l2);
    }

    private ListNode mergeList(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        if (l1.val > l2.val) {
            ListNode temp = l1;
            l1 = l2;
            l2 = temp;
        }

        l1.next = mergeList(l1.next, l2);
        return l1;
    }
}
