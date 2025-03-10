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

    private fun swap(cur: ListNode?): ListNode? {
        if (cur?.next == null) return cur
        val next = cur.next
        cur.next = next.next
        next.next = cur
        cur.next = swap(cur.next)
        return next
    }
}

// 1 -> 2 -> 3 -> 4
// 1 <- 2