package com.example

class SlidingWindowMaximum239_2 {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        val arr = IntArray(nums.size - k + 1)
        val deq = ArrayDeque<IntArray>()
        for (i in 0 until k - 1) {
            while (deq.isNotEmpty() && deq.last()[0] <= nums[i]) {
                deq.removeLast()
            }
            deq.addLast(intArrayOf(nums[i], i))
        }
        for (i in k - 1 until nums.size) {
            while (deq.isNotEmpty() && deq.first()[1] <= i - k) {
                deq.removeFirst()
            }
            while (deq.isNotEmpty() && deq.last()[0] <= nums[i]) {
                deq.removeLast()
            }
            deq.add(intArrayOf(nums[i], i))
            arr[i - k + 1] = deq.first()[0]
        }
        return arr
    }
}
