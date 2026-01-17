package com.example

import kotlin.math.sqrt

class Programmers92335_2 {
    fun solution(n: Int, k: Int): Int {
        val kNumber = convertToK(n, k)
        val numbers = kNumber
            .split("0")
            .filter { it != "" }
            .map { it.toLong() }
            .filter { isPrimeNumber(it) }
        return numbers.size
    }

    private fun convertToK(n: Int, k: Int): String {
        var num = n
        val sb = StringBuilder()
        while (num > 0) {
            sb.insert(0, num % k)
            num /= k
        }
        return sb.toString()
    }

    private fun isPrimeNumber(n: Long): Boolean {
        if (n == 1L) {
            return false
        }
        val sqrt = sqrt(n.toDouble()).toInt()
        for (i in 2..sqrt) {
            if (n % i == 0L) {
                return false
            }
        }
        return true
    }
}
