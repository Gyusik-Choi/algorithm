package com.example

class LargestNumber179_2 {
    fun largestNumber(nums: IntArray): String {
        val sortedNums = nums
            .sortedWith { num1, num2 ->
                (num2.toString() + num1.toString()).compareTo((num1.toString() + num2.toString()))
            }
        return if (sortedNums[0] == 0) "0" else sortedNums.joinToString("")
    }
}
