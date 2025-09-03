package com.example

class SwapNodesInPair24_2 {
    fun swapPairs(head: ListNode?): ListNode? {
        val root = ListNode()
        root.next = head
        var prev = root
        var cur = head
        // prev 는 cur.next 를 보고
        // cur 는 cur.next.next 를 보고
        // cur.next 는 cur 를 본다
        while (cur != null && cur.next != null) {
            val next = cur.next
            prev.next = next
            cur.next = next.next
            next.next = cur

            prev = cur
            cur = cur.next
        }
        return root.next
    }
}
