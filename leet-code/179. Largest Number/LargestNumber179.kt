package com.example

class LargestNumber179 {
    fun largestNumber(nums: IntArray): String {
        val sortedNums = nums.sortedWith { o1, o2 ->
            (o2.toString() + o1.toString()).toLong().compareTo((o1.toString() + o2.toString()).toLong())
        }
        return sortedNums.joinToString("")
    }
}
