package com.example

class ReverseLinkedListII92 {
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        val root = ListNode(0)
        root.next = head
        var pre = root
        var cur = head

        for (i in 1..<left) {
            pre = cur!!
            cur = cur.next
        }

        val curRef = cur
        var prev: ListNode? = null
        for (i in left until right + 1) {
            val next = cur!!.next
            cur.next = prev
            prev = cur
            cur = next
        }

        pre.next = prev
        curRef!!.next = cur
        return root.next
    }
}
