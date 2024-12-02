package com.example;

public class InsertionSortList147_2 {
    public ListNode insertionSortList(ListNode head) {
        // 루트를 가리키는 변수 선언, 나중에 parent.next를 결과로 리턴
        ListNode parent = new ListNode();
        // 정렬을 끝낸 대상을 가리키는 포인터
        // (head 는 정렬을 해야 할 대상을 가리키는 포인터)
        ListNode p = parent;

        // 다음 노드가 없을 때까지 순회
        while (head != null) {
            // p 의 next 값이 head 보다 작다면 계속 이동
            // p 는 정렬 되었기 때문에
            // p 가 마지막이 아니라면 p 와 p 의 next 사이에 넣을 head 값을 찾거나
            // p 가 마지막까지 갔다면 p 의 next 로 올 head 값을 찾는다
            while (p.next != null && p.next.val < head.val) p = p.next;

            // p 와 head 의 다음 노드
            ListNode pNext = p.next;
            ListNode headNext = head.next;

            // p 와 head 의 next 를 교환
            // (p 의 next 가 head 를 보고
            // head 의 next 는 기존 p 의 next 를 본다)
            p.next = head;
            head.next = pNext;

            // head 는 기존에 가리키던 다음 노드로 이동
            head = headNext;

            // p 를 맨 앞으로 보내는 이유는
            // parent 사이에 넣을 head 의 위치를 찾기 위해서인데
            // 이미 head 가 p 보다 크다면 p 를 맨 앞으로 보낼 필요가 없다
            // p 가 head 보다 커서 head 를 넣을 p 앞의 위치를 찾아야 할 때만
            // p 를 parent 로 보낸다
            if (head != null && p.val > head.val) p = parent;
        }
        return parent.next;
    }
}
