package com.example

class ReverseLinkedList206_2 {
    fun reverseList(head: ListNode?): ListNode? {
        return reverse(head, null)
    }

    private fun reverse(cur: ListNode?, prev: ListNode?): ListNode? {
        if (cur == null) return prev
        val next = cur.next
        cur.next = prev
        return reverse(next, cur)
    }
}