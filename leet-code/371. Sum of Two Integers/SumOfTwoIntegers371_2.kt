package com.example

class SumOfTwoIntegers371_2 {
    fun getSum(a: Int, b: Int): Int {
        val binaryA = String.format("%32s", a.toUInt().toString(radix = 2)).replace(" ", "0")
        val binaryB = String.format("%32s", b.toUInt().toString(radix = 2)).replace(" ", "0")
        var sum = 0
        var carry = 0
        var answer = StringBuilder()
        for (i in 31 downTo 0) {
            val numA = binaryA[i].code - '0'.code
            val numB = binaryB[i].code - '0'.code
            sum = (numA xor numB) xor carry
            carry = ((numA xor numB) and carry) or (numA and numB)
            answer.insert(0, sum)
        }
        println(answer.toString())
        return Integer.parseUnsignedInt(answer.toString(), 2)
    }
}
