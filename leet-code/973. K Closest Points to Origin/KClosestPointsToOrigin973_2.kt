package com.example

import java.util.PriorityQueue

class KClosestPointsToOrigin973_2 {
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        val pq = PriorityQueue<Node>(Comparator.comparingInt { it.distance })
        points.forEach { pq.add(Node(it)) }
        val answer = mutableListOf<IntArray>()
        IntArray(k).forEach { _ -> answer.add(pq.poll().point) }
        return answer.toTypedArray()
    }

    class Node(val point: IntArray) {
        val distance: Int = point[0] * point[0] + point[1] * point[1]
    }
}
