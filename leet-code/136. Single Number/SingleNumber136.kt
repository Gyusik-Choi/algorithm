package com.example

class SingleNumber136_3 {
    fun singleNumber(nums: IntArray): Int {
        return nums.reduce { acc, cur -> acc xor cur }
    }
}
