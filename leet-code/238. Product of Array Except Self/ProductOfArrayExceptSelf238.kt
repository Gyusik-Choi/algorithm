package com.example

class ProductOfArrayExceptSelf238 {
    fun productExceptSelf(nums: IntArray): IntArray {
        val answer: IntArray = IntArray(nums.size)

        var total = 1
        // https://kotlinlang.org/docs/ranges.html#ranges
        for (i in nums.indices) {
            answer[i] = total
            total *= nums[i]
        }
        total = 1
        for (i in nums.size - 1 downTo 0) {
            answer[i] *= total
            total *= nums[i]
        }

        return answer
    }
}