package com.example

class SortList148 {
    fun sortList(head: ListNode?): ListNode? {
        if (head == null || head.next == null) {
            return head
        }
        var prev = head
        // slow 를 기준으로 절반으로 나뉜다
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            prev = slow
            slow = slow!!.next
            fast = fast.next.next
        }
        // slow 와의 연결을 끊는다
        prev.next = null

        val low = sortList(head)
        val high = sortList(slow)
        return mergeTwoNodes(low, high)
    }

    private fun mergeTwoNodes(node1: ListNode?, node2: ListNode?): ListNode? {
        if (node1 == null) {
            return node2
        }
        if (node2 == null) {
            return node1
        }
        var n1 = node1
        var n2 = node2
        if (n1.`val` > n2.`val`) {
            val temp = n1
            n1 = n2
            n2 = temp
        }
        n1.next = mergeTwoNodes(n1.next, n2)
        return n1
    }
}
