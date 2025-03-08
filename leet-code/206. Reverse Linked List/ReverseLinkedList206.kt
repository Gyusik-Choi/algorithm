package com.example

class ReverseLinkedList206 {
    fun reverseList(head: ListNode?): ListNode? {
        return reverse(head, null)
    }

    private fun reverse(cur: ListNode?, rev: ListNode?): ListNode? {
        if (cur == null) {
            return rev
        }

        var current = cur
        val prev = current
        current = cur.next
        prev.next = rev
        return reverse(current, prev)
    }
}