package com.example

class Programmers43238_2 {
    fun solution(n: Int, times: IntArray): Long {
        var left = 0L
        // var right = (n * times.max() / times.size).toLong()
        // 위의 코드는 오버플로우가 발생할 수 있음
        var right = times.max().toLong() * n / times.size
        while (left < right) {
            val mid = left + (right - left) / 2
            if (n <= getTotal(times, mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }

    private fun getTotal(times: IntArray, time: Long): Long {
        return times.fold(0L) { acc, cur -> acc + time / cur }
    }
}
