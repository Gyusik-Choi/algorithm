package com.example.algorithm

class NumberOf1Bits191_2 {
    fun hammingWeight(n: Int): Int {
        var num = n
        var count = 0
        while (num > 0) {
            if (num % 2 == 1) {
                count += 1
            }
            num /= 2
        }
        return count
    }
}
