package com.example

class InsertionSortList147_2 {
    fun insertionSortList(head: ListNode?): ListNode? {
        val parent = ListNode()
        var p = parent
        var h = head

        while (h != null) {
            while (p.next != null && p.next.`val` < h.`val`) {
                p = p.next
            }
            val pNext = p.next
            val hNext = h.next
            p.next = h
            h.next = pNext
            h = hNext

            if (h != null && p.`val` > h.`val`) {
                p = parent
            }
        }

        return parent.next
    }
}
