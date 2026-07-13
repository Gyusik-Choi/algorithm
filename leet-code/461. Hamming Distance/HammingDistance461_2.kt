package com.example

import kotlin.math.abs
import kotlin.math.max

class HammingDistance461_2 {
    fun hammingDistance(x: Int, y: Int): Int {
        val binary1 = convertToBinaryString(x)
        val binary2 = convertToBinaryString(y)
        val maxLength = max(binary1.length, binary2.length)
        val paddedBinary1 = padLeft(binary1, maxLength)
        val paddedBinary2 = padLeft(binary2, maxLength)
        return IntRange(0, maxLength - 1)
            .map { if (paddedBinary1[it] != paddedBinary2[it]) 1 else 0 }
            .filter { it == 1 }
            .size
    }

    private fun convertToBinaryString(num: Int): String {
        var number = num
        val sb = StringBuilder()
        while (number > 0) {
            sb.insert(0, number % 2)
            number /= 2
        }
        return sb.toString()
    }

    private fun padLeft(binary: String, length: Int): String {
        val binaryLength = binary.length
        val diff = abs(binaryLength - length)
        val sb = StringBuilder(binary)
        for (i in 0 until diff) {
            sb.insert(0, "0")
        }
        return sb.toString()
    }
}
