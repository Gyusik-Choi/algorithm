package com.example

import kotlin.math.sqrt

class Programmers92335_3 {
    fun solution(n: Int, k: Int): Int {
        val kDigit = convertToKDigit(n, k)
        val kDigits = kDigit.split(Regex("0+")).filter { it.isNotBlank() }
        return kDigits.filter { isPrime(it.toLong()) }.size
    }

    private fun convertToKDigit(n: Int, k: Int): String {
        var num = n
        val sb = StringBuilder()
        while (num > 0) {
            sb.insert(0, num % k)
            num /= k
        }
        return sb.toString()
    }

    private fun isPrime(num: Long): Boolean {
        if (num < 2) return false
        val sqrt = sqrt(num.toDouble()).toInt()
        for (i in 2..sqrt) if (num % i == 0L) return false
        return true
    }
}
