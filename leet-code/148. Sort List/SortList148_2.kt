package com.example

class SortList148_2 {
    fun sortList(head: ListNode?): ListNode? {
        if (head == null || head.next == null) return head
        var prev: ListNode? = null
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            prev = slow
            slow = slow!!.next
            fast = fast.next!!.next
        }
        prev!!.next = null
        val left = sortList(head)
        val right = sortList(slow)
        return mergeList(left, right)
    }

    private fun mergeList(l1: ListNode?, l2: ListNode?): ListNode? {
        if (l1 == null || l2 == null) {
            return l1 ?: l2
        }
        var list1 = l1
        var list2 = l2
        if (list1.`val` > list2.`val`) {
            val temp = list1
            list1 = list2
            list2 = temp
        }
        val list = mergeList(list1.next, list2)
        list1.next = list
        return list1
    }
}
