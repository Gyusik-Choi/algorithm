package com.example

class ClimbingStairs70_3 {
    private val map = mutableMapOf(0 to 0, 1 to 1, 2 to 2, 3 to 3)

    fun climbStairs(n: Int): Int {
        if (map.containsKey(n)) return map[n]!!
        map[n] = climbStairs(n - 1) + climbStairs(n - 2)
        return map[n]!!
    }
}
