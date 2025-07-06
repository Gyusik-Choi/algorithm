package com.example

class TwoSumInputArrayIsSorted167 {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var low = 0
        var high = numbers.size - 1
        val answer = IntArray(2)
        while (low < high) {
            if (numbers[low] + numbers[high] == target) {
                // 문제에서 요구하는 인덱스는 1부터 시작한다
                answer[0] = low + 1
                answer[1] = high + 1
                break
            }

            if (numbers[low] + numbers[high] < target) {
                low += 1
            } else {
                high -= 1
            }
        }
        return answer
    }
}
