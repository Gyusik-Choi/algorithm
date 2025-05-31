package com.example

class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        val pq = java.util.PriorityQueue<Int>(java.util.Collections.reverseOrder())
        for (num in nums) {
            pq.add(num)
        }
        repeat(k - 1) { pq.poll() }
        return pq.poll()
    }
}
