package com.example

import java.util.*

class NetworkDelayTime743_2 {
    fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
        val map = mutableMapOf<Int, MutableList<IntArray>>()
        times.forEach {
            map.putIfAbsent(it[0], mutableListOf())
            map[it[0]]!!.add(intArrayOf(it[1], it[2]))
        }
        val minTimes = IntArray(n + 1)
        minTimes.fill(Int.MAX_VALUE)
        minTimes[0] = 0
        minTimes[k] = 0
        val visited = BooleanArray(n + 1)
        // IntArray -> 정점, 시간(현재 정점으로 오는데 걸리는 시간)
        val pq = PriorityQueue<IntArray> { o1, o2 -> o1[1] - o2[1] }
        pq.add(intArrayOf(k, 0))
        while (pq.isNotEmpty()) {
            val start = pq.poll()
            if (visited[start[0]]) {
                continue
            }
            visited[start[0]] = true
            if (!map.containsKey(start[0])) {
                continue
            }
            for (end in map[start[0]]!!) {
                if (visited[end[0]]) {
                    continue
                }
                if (minTimes[end[0]] <= start[1] + end[1]) {
                    continue
                }
                minTimes[end[0]] = start[1] + end[1]
                pq.add(intArrayOf(end[0], minTimes[end[0]]))
            }
        }
        return if (minTimes.any { it == Int.MAX_VALUE }) -1 else minTimes.filterIndexed { i, _ -> i != 0 && i != k }
            .max()
    }
}
