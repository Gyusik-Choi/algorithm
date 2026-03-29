package com.example

class JewelsAndStones771_2 {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        val set = mutableSetOf<Char>()
        jewels.forEach { set.add(it) }
        return stones.filter { set.contains(it) }.length
    }
}
