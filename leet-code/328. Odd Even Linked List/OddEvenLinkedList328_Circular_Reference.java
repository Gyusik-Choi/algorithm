public class OddEvenLinkedList328_Circular_Reference {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;

        while (odd != null && odd.next != null) {
            odd.next = odd.next.next;
            odd = odd.next;
        }

        // 위의 while 문에 의해
        // even 이 이미 2 -> 3 -> 5 로 변경된 상태다
        while (even != null && even.next != null) {
            even.next = even.next.next;
            even = even.next;
        }

        // while 문을 마치면
        // even 은 2 -> 5 가 된다
        // odd 와 even.next 는 같은 주소의 5를 참조하고 있다
        // odd.next 에 even 을 할당하면
        // 순환 참조가 된다
        odd.next = evenHead;
        return head;
    }
}
