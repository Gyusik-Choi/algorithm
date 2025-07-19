package com.example

class SlidingWindowMaximum239 {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        val answer = mutableListOf<Int>()
        val deq = ArrayDeque<Int>()
        for (i in nums.indices) {
            if (!deq.isEmpty() && deq.first() < i - k + 1) {
                deq.removeFirst()
            }
            while (!deq.isEmpty() && nums[deq.last()] < nums[i]) {
                deq.removeLast()
            }
            deq.addLast(i)
            if (i >= k - 1) {
                answer.add(nums[deq.first()])
            }
        }
        return answer.toIntArray()
    }
}
