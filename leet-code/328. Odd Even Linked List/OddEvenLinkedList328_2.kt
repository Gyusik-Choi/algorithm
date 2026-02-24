package com.example

class OddEvenLinkedList328_2 {
    fun oddEvenList(head: ListNode?): ListNode? {
        if (head == null) {
            return null
        }
        var odd: ListNode = head
        var even = odd.next
        val evenRef = even
        while (even?.next != null) {
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        }
        odd.next = evenRef
        return head
    }
}
