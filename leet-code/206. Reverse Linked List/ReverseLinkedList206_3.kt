package com.example

class ReverseLinkedList206_3 {
    fun reverseList(head: ListNode?): ListNode? {
        var cur = head
        var reversedHead: ListNode? = null
        while (cur != null) {
            val next = cur.next
            cur.next = reversedHead
            reversedHead = cur
            cur = next
        }
        return reversedHead
    }
}
