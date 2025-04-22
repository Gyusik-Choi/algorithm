package com.example

import java.util.PriorityQueue

class TopKFrequentElements347 {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val counts = mutableMapOf<Int, Int>()
        for (num in nums) {
            counts[num] = counts.getOrDefault(num, 0) + 1
        }
        val pq = PriorityQueue<IntArray>(Comparator { o1, o2 -> o2[1] - o1[1] })
        for (entry in counts) {
            pq.add(intArrayOf(entry.key, entry.value))
        }
        val answer = IntArray(k)
        for (i in 0..k - 1) {
            answer[i] = pq.poll()[0]
        }
        return answer
    }
}
