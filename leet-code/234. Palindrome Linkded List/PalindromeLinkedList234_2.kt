package com.example

class PalindromeLinkedList234_2 {
    fun isPalindrome(head: ListNode?): Boolean {
        var prev: ListNode? = null
        var slow = head
        var fast = head
        while (fast?.next != null) {
            prev = slow
            slow = slow!!.next
            fast = fast.next!!.next
        }
        // 연결 끊기
        prev?.next = null

        prev = null
        while (slow != null) {
            var next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        }
        slow = prev

        var cur = head
        while (cur != null) {
            if (cur.`val` != slow!!.`val`) {
                return false
            }
            cur = cur.next
            slow = slow.next
        }
        return true
    }
}
