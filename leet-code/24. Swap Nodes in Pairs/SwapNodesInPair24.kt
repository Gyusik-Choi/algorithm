package com.example

class SwapNodesInPair24 {
    fun swapPairs(head: ListNode?): ListNode? {
        if (head?.next == null) return head
        val next = head.next
        head.next = next.next
        next.next = head
        head.next = swapPairs(head.next)
        return next
    }
}
