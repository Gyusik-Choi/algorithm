package com.example

class ReverseLinkedListII92_2 {
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        var prev: ListNode? = null
        var cur = head
        for (i in 0 until left - 1) {
            prev = cur
            cur = cur?.next
        }
        val curRef = cur
        var front: ListNode? = null
        for (i in 0 until right - left + 1) {
            val next = cur?.next
            cur?.next = front
            front = cur
            cur = next
        }
        if (prev != null) {
            prev.next = front
        }
        curRef?.next = cur
        // head 부터 뒤집는 경우
        // 연결 리스트의 시작점이 head 가 아니기 때문에 head 를 리턴하면 안 된다
        return if (prev == null) front else head
    }
}
