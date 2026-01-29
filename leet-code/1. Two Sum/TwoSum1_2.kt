package com.example.algorithm

class TwoSum1_2 {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val sortedNums = nums
            .mapIndexed { index, value -> intArrayOf(value, index)}
            .sortedBy { it[0] }
        var left = 0
        var right = nums.size - 1
        while (left < right) {
            val sums = sortedNums[left][0] + sortedNums[right][0]
            if (sums == target) {
                break
            }
            if (sums < target) {
                left += 1
            } else {
                right -= 1
            }
        }
        return intArrayOf(sortedNums[left][1], sortedNums[right][1])
    }
}
