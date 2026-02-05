package com.example.algorithm

class ArrayPartition561_3 {
    fun arrayPairSum(nums: IntArray): Int {
        return nums
            .sorted()
            .filterIndexed { i, _ -> i % 2 == 0 }
            .sum()
    }
}
