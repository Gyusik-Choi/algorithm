package com.example

class ReverseLinkedList206_2 {
    fun reverseList(head: ListNode?): ListNode? {
        return reverse(head, null)
    }

    private fun reverse(cur: ListNode?, rev: ListNode?): ListNode? {
        if (cur == null) return rev
        val next = cur.next
        cur.next = rev
        return reverse(next, cur)
    }
}