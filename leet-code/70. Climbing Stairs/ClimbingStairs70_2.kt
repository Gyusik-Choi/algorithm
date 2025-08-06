package com.example

class ClimbingStairs70_2 {
    private val memo = IntArray(46)

    fun climbStairs(n: Int): Int {
        if (memo[n] != 0) {
            return memo[n]
        }
        if (n < 2) {
            return 1
        }
        memo[n] = climbStairs(n - 2) + climbStairs(n - 1)
        return memo[n]
    }
}
