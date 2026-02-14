package com.example

class PalindromeLinkedList234_3 {
    fun isPalindrome(head: ListNode?): Boolean {
        var prev: ListNode? = null
        var cur: ListNode? = head
        var next: ListNode? = head
        while (next != null && next.next != null) {
            prev = cur
            cur = cur?.next
            next = next.next.next
        }
        prev?.next = null
        if (next != null) {
            cur = cur?.next
        }

        var front: ListNode? = null
        while (cur != null) {
            val next = cur.next
            cur.next = front
            front = cur
            cur = next
        }

        var node: ListNode? = head
        while (node != null && front != null && node.`val` == front.`val`) {
            node = node.next
            front = front.next
        }
        return front == null
    }
}