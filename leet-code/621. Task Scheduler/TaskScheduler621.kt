package com.example.algorithm

import java.util.PriorityQueue

class TaskScheduler621 {
    fun leastInterval(tasks: CharArray, n: Int): Int {
        // task 는 배열로 정리해서
        // 첫번째 인덱스는 동일 label 의 갯수
        // 두번째 인덱스는 label
        //
        // 여러번 우선순위 큐에서 넣고 꺼내는 횟수를 줄이고
        // 시간 초과를 방지하기 위해
        // task 의 갯수만큼 우선순위 큐에 모두 넣는게 아니라
        // 동일한 라벨은 하나의 요소로 합치고 갯수로 관리한다
        //
        // 우선순위 큐의 peek 에 있는 task 를 꺼낸다
        // 해당 task 가
        // 처리될 수 있으면 리스트에 담고
        // 처리될 수 없으면 idle 로 처리한다
        // task 는 다시 우선순위 큐로 넣는다
        val pq = PriorityQueue<Array<String>> { o1, o2 ->
          when {
              o1[0] == o2[0] -> o1[1].compareTo(o2[1])
              else -> o2[0].toInt() - o1[0].toInt()
          }
        }
        val cnt = mutableMapOf<String, Int>()
        for (task in tasks) {
            cnt[task.toString()] = cnt.getOrDefault(task.toString(), 0) + 1
        }
        val list = cnt.keys.map { arrayOf(cnt[it]!!.toString(), it) }
        pq.addAll(list)

        val completedTask = mutableListOf<String>()
        while (!pq.isEmpty()) {
            val temp = mutableListOf<Array<String>>()
            while (!pq.isEmpty()) {
                val item = pq.poll()
                val interval = Math.min(completedTask.size, n)
                if (isValid(completedTask, item, interval)) {
                    completedTask.add(item[1])
                    if (item[0].toInt() - 1 > 0) {
                        pq.add(arrayOf((item[0].toInt() - 1).toString(), item[1]))
                    }
                    break
                }
                temp.add(item)
                // 해당 사이클에 들어갈 수 있는 task 가 없을 경우 idle
                if (pq.isEmpty()) {
                    completedTask.add("0")
                }
            }
            pq.addAll(temp)
        }
        return completedTask.size
    }

    private fun isValid(list: MutableList<String>, target: Array<String>, interval: Int): Boolean {
        for (i in list.size - interval..list.size - 1) {
            if (list[i] == target[1]) {
                return false
            }
        }
        return true
    }
}