package com.example

import java.util.PriorityQueue

class MergeKSortedLists23_2 {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        val pq = PriorityQueue<ListNode> { i1, i2 -> i1.`val` - i2.`val` }
        lists.forEach { if (it != null) pq.add(it) }
        val root = ListNode()
        var cur = root
        while (!pq.isEmpty()) {
            val item = pq.poll()
            val itemNext = item.next
            item.next = null
            cur.next = item
            cur = cur.next
            if (itemNext != null) {
                pq.add(itemNext)
            }
        }
        return root.next
    }
}