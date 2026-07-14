package com.example

class MinimumBitFlipsToConvertNumber2220 {
    fun minBitFlips(start: Int, goal: Int): Int {
        return (start xor goal).countOneBits()
    }
}
