package com.example

import java.util.PriorityQueue

class QueueReconstructionByHeight406 {
    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {
        val pq = PriorityQueue<IntArray> { p1, p2 ->
            when {
                p1[0] == p2[0] -> p1[1] - p2[1]
                else -> p1[0] - p2[0]
            }
        }
        pq.addAll(people)

        val answer = mutableListOf<IntArray>()
        val temp = mutableListOf<IntArray>()
        while (!pq.isEmpty()) {
            val person = pq.poll()
            if (isValid(answer, person)) {
                answer.add(person)
                pq.addAll(temp)
                temp.clear()
                continue
            }
            temp.add(person)
        }
        return answer.toTypedArray()
    }

    private fun isValid(list: MutableList<IntArray>, person: IntArray): Boolean {
        var count = 0
        for (item in list) {
            if (item[0] >= person[0]) {
                count += 1
            }
        }
        return count == person[1]
    }
}

// [4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]
// [4, 4] 뽑고 조건에 맞지 않아서 우선순위 큐에서 다시 꺼낸다
// [5, 0] 뽑고 조건에 맞아서 선택한다 그리고 앞서 뽑은 [4, 4] 는 다시 우선순위 큐에 넣는다
// -> [5, 0]
