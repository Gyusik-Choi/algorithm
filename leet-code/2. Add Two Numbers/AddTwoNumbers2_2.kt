package com.example

class AddTwoNumbers2_2 {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        return add(l1, l2, 0)
    }

    private fun add(l1: ListNode?, l2: ListNode?, carry: Int): ListNode? {
        if (l1 == null && l2 == null) {
            return if (carry == 0) null else ListNode(carry)
        }
        val sum = (l1?.`val` ?: 0) + (l2?.`val` ?: 0)
        val node = ListNode((sum + carry) % 10)
        node.next = add(l1?.next, l2?.next, (sum + carry) / 10)
        return node
    }
}
