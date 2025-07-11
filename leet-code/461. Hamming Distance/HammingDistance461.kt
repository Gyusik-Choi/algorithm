package com.example

class HammingDistance461 {
    fun hammingDistance(x: Int, y: Int): Int {
        return (x xor y).countOneBits()
    }
}
