package com.example.algorithm

import java.util.PriorityQueue

class Programmers42628 {
    fun solution(operations: Array<String>): IntArray {
        val maxHeap = PriorityQueue<Int>{ o1, o2 -> o2 - o1 }
        val minHeap = PriorityQueue<Int>{ o1, o2 -> o1 - o2 }
        val remove = mutableMapOf<Int, Int>()
        for (operation in operations) {
            val o = operation.split(" ")
            val command = o[0]
            val data = o[1].toInt()
            if (command == "I") {
                maxHeap.add(data)
                minHeap.add(data)
                remove.putIfAbsent(data, 0)
                remove.put(data, remove[data]!! + 1)
            } else {
                if (data == -1) {
                    // maxHeap 에서만 빼서
                    // minHeap 에 남아있는 것처럼 보이지만
                    // 실제로는 minHeap 이 비어있는게 맞을 수 있다
                    normalizePriorityQueue(minHeap, remove)
                    val num = minHeap.poll()
                    // https://www.baeldung.com/kotlin/map-modify-in-place
                    remove.computeIfPresent(num) {_, v -> v - 1}

                } else {
                    // minHeap 에서만 빼서
                    // maxHeap 에 남아있는 것처럼 보이지만
                    // 실제로는 maxHeap 이 비어있는게 맞을 수 있다
                    normalizePriorityQueue(maxHeap, remove)
                    val num = maxHeap.poll()
                    remove.computeIfPresent(num) {_, v -> v - 1}
                }
            }
        }

        normalizePriorityQueue(minHeap, remove)
        normalizePriorityQueue(maxHeap, remove)

        if (maxHeap.isEmpty() || minHeap.isEmpty()) {
            return intArrayOf(0, 0)
        }
        return intArrayOf(maxHeap.peek(), minHeap.peek())
    }

    private fun normalizePriorityQueue(pq: PriorityQueue<Int>, map: MutableMap<Int, Int>): Unit {
        while (pq.isNotEmpty() && map.containsKey(pq.peek()) && map[pq.peek()] == 0) {
            pq.poll()
        }
    }
}
