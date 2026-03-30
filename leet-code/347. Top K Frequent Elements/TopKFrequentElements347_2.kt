package com.example

import java.util.PriorityQueue

class TopKFrequentElements347_2 {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        nums.forEach { map[it] = map.getOrDefault(it, 0) + 1 }
        val pq = PriorityQueue<Element>(compareByDescending { it.value })
        map.forEach { entry -> pq.add(Element(entry.key, entry.value)) }
        val answer = IntArray(k)
        IntRange(1, k).forEachIndexed { i, _ ->  answer[i] = pq.poll()!!.key }
        return answer
    }

    private data class Element(val key: Int, val value: Int)
}
