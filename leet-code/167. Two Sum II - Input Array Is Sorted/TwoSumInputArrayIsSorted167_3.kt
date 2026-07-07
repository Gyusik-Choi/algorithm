package com.example

class TwoSumInputArrayIsSorted167_3 {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var low = 0
        var high = numbers.lastIndex
        while (low < high) {
            val sum = numbers[low] + numbers[high]
            when {
                sum < target -> low++
                sum > target -> high--
                else -> break
            }
        }
        return intArrayOf(low + 1, high + 1)
    }
}
