package com.example

import kotlin.math.sqrt

class Programmers92335 {

    fun solution(n: Int, k: Int): Int {
        var answer = 0
        val kNumber = convertToKNumber(n, k)
        val splitKNumber = kNumber.split("0")
        for (num in splitKNumber) {
            if (num == "") {
                continue
            }
            if (isPrimeNumber(num.toLong())) {
                answer += 1
            }
        }
        return answer
    }

    private fun convertToKNumber(n: Int, k: Int): String {
        val kNumber = StringBuilder()
        var decimalNumber = n
        while (decimalNumber > 0) {
            kNumber.append(decimalNumber % k)
            decimalNumber /= k
        }
        return kNumber.reverse().toString()
    }

    private fun isPrimeNumber(n: Long): Boolean {
        if (n == 1L) {
            return false
        }
        val squareRoot = sqrt(n.toDouble()).toInt()
        for (i in 3..squareRoot) {
            if (n % i == 0L) {
                return false
            }
        }
        return true
    }

    // 진수 변환
    // 0을 기준으로 분리
    // 소수 여부 판단
}