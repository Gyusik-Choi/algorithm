package com.example

class OddEvenLinkedList328 {
    fun oddEvenList(head: ListNode?): ListNode? {
        if (head == null || head.next == null) {
            return head
        }
        var odd = head
        var even = head.next
        val evenRef = even
        while (even != null && even.next != null) {
            odd!!.next = even.next
            even.next = even.next.next
            // 1->2->3->4
            // 1->2->3

            odd = odd.next
            even = even.next
        }
        odd.next = evenRef
        return head
    }
}
