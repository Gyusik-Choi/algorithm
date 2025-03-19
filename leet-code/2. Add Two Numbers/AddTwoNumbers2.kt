package com.example

class AddTwoNumbers2 {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var list1 = l1
        var list2 = l2
        val root = ListNode(0)
        // 올림수
        var carry = 0
        var cur = root
        while (list1 != null || list2 != null || carry != 0) {
            // 현재합
            var sum = 0
            if (list1 != null) {
                sum += list1.`val`
                list1 = list1.next
            }

            if (list2 != null) {
                sum += list2.`val`
                list2 = list2.next
            }

            sum += carry
            carry = sum / 10
            val remainder = sum % 10
            cur.next = ListNode(remainder)
            cur = cur.next!!
        }
        return root.next
    }
}
