package com.example

import java.util.PriorityQueue

class MergeIntervals56 {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        val pq = PriorityQueue<IntArray> { o1, o2 ->
            if (o1[0] == o2[0]) {
                o1[1] - o2[1]
            } else {
                o1[0] - o2[0]
            }
        }
        for (interval in intervals) {
            pq.add(interval)
        }

        val answer = mutableListOf<IntArray>()
        while (!pq.isEmpty()) {
            val item = pq.poll()
            if (answer.isEmpty()) {
                answer.add(item)
            } else {
                val lastList = answer.last()
                if (lastList[1] < item[0]) {
                    answer.add(item)
                } else {
                    if (lastList[1] < item[1]) {
                        answer.last()[1] = item[1]
                    }
                }
            }
        }
        return answer.toTypedArray()
    }

    // [1, 4] [2, 3] [3, 5] [6, 9] [8, 10]
    // [1, 4] [4, 4] [4, 5] [6, 9] [9, 10]
    // [1, 5] [6, 10]

    // 우선순위 큐
    // [1, 4] -> [1, 4]
    // [1, 4] [2, 3] -> [1, 4]
    // [1, 4] [3, 5] -> [1, 5]
    // [1, 5] [6, 9] -> [1, 5] [6, 9]
    // [1, 5] [6, 9] [8, 10] -> [1, 5] [6, 10]
}
