package com.example

class CombinationSum39_2 {
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        var sums = 0

        fun recursion(
            combs: MutableList<List<Int>>,
            comb: MutableList<Int>,
            idx: Int,
        ): List<List<Int>> {
            if (sums >= target) {
                if (sums == target) {
                    combs.add(comb.toList())
                }
                return combs
            }
            for (i in idx until candidates.size) {
                comb.add(candidates[i])
                sums += candidates[i]
                recursion(combs, comb, i)
                sums -= candidates[i]
                comb.removeLast()
            }
            return combs
        }

        return recursion(mutableListOf(), mutableListOf(), 0)
    }
}
