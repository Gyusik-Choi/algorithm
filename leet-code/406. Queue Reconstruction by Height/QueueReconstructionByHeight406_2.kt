package com.example

import java.util.PriorityQueue

class QueueReconstructionByHeight406_2 {
    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {
        val pq = PriorityQueue<IntArray> { p1, p2 ->
            when {
                p1[0] == p2[0] -> p1[1] - p2[1]
                else -> p2[0] - p1[0]
            }
        }
        pq.addAll(people)

        val answer = mutableListOf<IntArray>()
        while (!pq.isEmpty()) {
            val item = pq.poll()
            answer.add(item[1], item)
        }
        return answer.toTypedArray()
    }
}
