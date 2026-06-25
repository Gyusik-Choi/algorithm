package com.example

class InsertionSortList147_3 {
    fun insertionSortList(head: ListNode?): ListNode? {
        var headNode = head
        val sortedNode = ListNode()
        while (headNode != null) {
            var cur = sortedNode
            while (cur.next != null && cur.next.`val` < headNode.`val`) {
                cur = cur.next
            }
            val temp = headNode
            headNode = headNode.next
            temp.next = null
            val curNext = cur.next
            cur.next = temp
            cur.next.next = curNext
        }
        return sortedNode.next
    }
}
