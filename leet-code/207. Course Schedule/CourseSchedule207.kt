package com.example.algorithm

class CourseSchedule207 {
    fun canFinish(
        numCourses: Int,
        prerequisites: Array<IntArray>,
    ): Boolean {
        val inDegree = IntArray(numCourses)
        // 자신보다 우선순위가 높은 요소들을 값으로 갖는다
        val map = mutableMapOf<Int, MutableList<Int>>()
        for (prerequisite in prerequisites) {
            val from = prerequisite[1]
            val to = prerequisite[0]
            inDegree[to] += 1
            map.putIfAbsent(to, mutableListOf())
            map[to]!!.add(from)
        }
        val deq = ArrayDeque<Int>()
        initDeq(inDegree, deq)

        while (!deq.isEmpty()) {
            val start = deq.removeFirst()
            for (entry in map.entries) {
                if (!entry.value.contains(start)) {
                    continue
                }
                inDegree[entry.key] -= 1
                if (inDegree[entry.key] == 0) {
                    deq.add(entry.key)
                }
            }
        }

        return inDegree.none { it -> it > 0 }
    }

    private fun initDeq(
        inDegree: IntArray,
        deq: ArrayDeque<Int>,
    ): ArrayDeque<Int> {
        for (i in inDegree.indices) {
            if (inDegree[i] == 0) {
                deq.add(i)
            }
        }
        return deq
    }
}
