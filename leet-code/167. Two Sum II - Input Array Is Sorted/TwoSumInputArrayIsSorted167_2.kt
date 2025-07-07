package com.example

class TwoSumInputArrayIsSorted167_2 {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        val answer = IntArray(2)
        for (idx1 in 0..numbers.size - 2) {
            val idx2 = getTarget(numbers, target, numbers[idx1], idx1)
            if (idx2 == 0) {
                continue
            }
            answer[0] = idx1 + 1
            answer[1] = idx2 + 1
            break
        }
        return answer
    }

    private fun getTarget(numbers: IntArray, target: Int, num1: Int, idx: Int): Int {
        var low = idx + 1
        var high = numbers.size - 1
        while (low <= high) {
            val mid = low + (high - low) / 2
            val num2 = numbers[mid]
            if (num1 + num2 == target) {
                return mid
            }
            if (num1 + num2 < target) {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return 0
    }
}