package com.example

class NumberOf1Bits191_3 {
    fun hammingWeight(n: Int): Int {
        var num = n
        var count = 0
        while (num > 0) {
            if (num % 2 == 1) {
                count++
            }
            num /= 2
        }
        return count
    }
}
