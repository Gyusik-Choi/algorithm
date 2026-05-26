package com.example

import java.util.*

class KthLargestElementInAnArray215_3 {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        val pq = PriorityQueue<Int>(Comparator { o1, o2 -> o2 - o1 })
        pq.addAll(nums.asIterable())
        IntRange(0, k - 2).forEach { _ -> pq.poll() }
        return pq.poll()
    }
}
