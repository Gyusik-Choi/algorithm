package com.example

class ProductOfArrayExceptSelf238_2 {
    fun productExceptSelf(nums: IntArray): IntArray {
        val answer = IntArray(nums.size)
        var p = 1
        for (i in nums.indices) {
            answer[i] = p
            p *= nums[i]
        }
        p = 1
        for (i in nums.size - 1 downTo 0) {
            answer[i] *= p
            p *= nums[i]
        }
        return answer
    }
}
