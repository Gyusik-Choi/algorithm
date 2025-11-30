package com.example

class Programmers43238 {
    fun solution(n: Int, times: IntArray): Long {
        var left: Long = 1
        // var right = (getMaxValue(times) * n).toLong()
        // 위처럼 곱한 후에 Long 타입으로 변환하면 안 된다
        // 곱셈에서 오버플로우가 발생할 수 있다
        var right = getMaxValue(times).toLong() * n
        while (left < right) {
            val mid = left + (right - left) / 2
            var total: Long = 0
            times.forEach { total += mid / it }
            if (total >= n) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }

    private fun getMaxValue(times: IntArray): Int {
        var maxValue = 0
        times.forEach {
            if (maxValue < it) {
                maxValue = it
            }
        }
        return maxValue
    }
}
