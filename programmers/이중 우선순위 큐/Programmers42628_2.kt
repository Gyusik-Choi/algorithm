package com.example.algorithm

import java.util.PriorityQueue

class Programmers42628_2 {
    fun solution(operations: Array<String>): IntArray {
        val maxHeap = PriorityQueue<Int> { o1, o2 -> o2 - o1 }
        val minHeap = PriorityQueue<Int> { o1, o2 -> o1 - o2 }
        for (operation in operations) {
            val o = operation.split(" ")
            val command = o[0]
            val data = o[1].toInt()
            if (command == "I") {
                maxHeap.add(data)
                minHeap.add(data)
            } else {
                if (data == -1) {
                    maxHeap.remove(minHeap.poll())
                } else {
                    minHeap.remove(maxHeap.poll())
                }
            }
        }
        if (maxHeap.isEmpty() || minHeap.isEmpty()) {
            return intArrayOf(0, 0)
        }
        return intArrayOf(maxHeap.peek(), minHeap.peek())
    }
}
