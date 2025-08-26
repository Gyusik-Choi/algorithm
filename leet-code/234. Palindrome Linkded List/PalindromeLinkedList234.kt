package com.example

import java.util.LinkedList

class PalindromeLinkedList234 {
    fun isPalindrome(head: ListNode?): Boolean {
        // 1 -> 2 -> 2 -> 1
        // 1 -> 2 -> 3 -> 2 -> 1
        // 짝수, 홀수
        // 런너
        var slow = head
        var fast = head
        while (fast?.next != null) {
            slow = slow!!.next
            fast = fast.next!!.next
        }

        val stack = LinkedList<Int>()
        while (slow != null) {
            stack.push(slow.`val`)
            slow = slow.next
        }

        var cur = head
        while (stack.isNotEmpty()) {
            if (stack.pop() != cur!!.`val`) {
                return false
            }
            cur = cur.next
        }
        return true
    }
}
