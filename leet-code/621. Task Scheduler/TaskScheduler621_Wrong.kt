package com.example

import java.util.PriorityQueue

class TaskScheduler621_Wrong {
    fun leastInterval(tasks: CharArray, n: Int): Int {
        // task 는 배열로 정리해서
        // 첫번째 인덱스는 동일 label 에서 번호
        // 두번째 인덱스는 label
        //
        // 우선순위 큐의 peek 에 있는 task 를 꺼낸다
        // 해당 task 가
        // 처리될 수 있으면 리스트에 담고
        // 처리될 수 없으면 idle 로 처리한다
        // task 는 다시 우선순위 큐로 넣는다
        val pq = PriorityQueue<CharArray> { o1, o2 ->
          when {
              o1[0] == o2[0] -> o1[1] - o2[1]
              else -> o2[0] - o1[0]
          }
        }
        val cnt = mutableMapOf<Char, Int>()
        for (task in tasks) {
            cnt[task] = cnt.getOrDefault(task, 0) + 1
        }
        val list = tasks.map {
            cnt[it] = cnt[it]!! - 1
            charArrayOf((cnt[it]!! + 1).toChar(), it)
        }
        pq.addAll(list)

        val completedTask = mutableListOf<Char>()
        while (!pq.isEmpty()) {
            val temp = mutableListOf<CharArray>()
            while (!pq.isEmpty()) {
                val item = pq.poll()
                val interval = Math.min(completedTask.size, n)
                if (!isValid(completedTask, item, interval)) {
                    temp.add(item)
                    continue
                }
                completedTask.add(item[1])
                pq.addAll(temp)
                break
            }
            if (temp.isNotEmpty()) {
                completedTask.add('0')
                pq.addAll(temp)
            }
        }
        return completedTask.size
    }

    private fun isValid(list: MutableList<Char>, target: CharArray, interval: Int): Boolean {
        for (i in list.size - interval..list.size - 1) {
            if (list[i] == target[1]) {
                return false
            }
        }
        return true
    }
}
// [B, C] / n = 3 / A
// [B, C, D, E, F, G] / n = 3 / A