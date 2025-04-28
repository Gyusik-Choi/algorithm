package com.example

class Combinations77_2 {
    fun combine(n: Int, k: Int): List<List<Int>> {
        val combinations = mutableListOf<List<Int>>()
        val comb = mutableListOf<Int>()

        fun getCombinations(cur: Int) {
            if (comb.size == k) {
                combinations.add(comb.toList())
                return
            }

            for (num in cur..n) {
                comb.add(num)
                getCombinations(num + 1)
                comb.removeLast()
            }
        }

        getCombinations(1)
        return combinations
    }
}