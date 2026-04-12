package com.example

class Combinations77_3 {
    fun combine(n: Int, k: Int): List<List<Int>> {
        fun recursion(combs: MutableList<List<Int>>, comb: MutableList<Int>, cur: Int): List<List<Int>> {
            if (comb.size == k) {
                combs.add(comb.toList())
                return combs
            }
            for (i in cur..n) {
                comb.add(i)
                recursion(combs, comb, i + 1)
                comb.removeLast()
            }
            return combs
        }

        return recursion(mutableListOf(), mutableListOf(), 1)
    }
}
