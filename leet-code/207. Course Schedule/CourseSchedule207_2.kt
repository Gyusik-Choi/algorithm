package com.example

class CourseSchedule207_2 {
    // dfs 탐색
    // 우선순위가 낮은 정점에서 우선순위가 높은 정점을 방문해나간다
    // 방문하는 과정에서 이미 지나친 정점을 만나면 순환 구조가 있다는 의미다
    // 시간초과에 걸리지 않도록 이미 방문을 완료한 정점은 해시맵으로 관리한다
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val map = mutableMapOf<Int, MutableList<Int>>()
        val toComplete = mutableSetOf<Int>()
        val completed = mutableSetOf<Int>()
        for (p in prerequisites) {
            map.putIfAbsent(p[0], mutableListOf())
            map[p[0]]!!.add(p[1])
        }
        for (k in map.keys) {
            if (!dfs(map, toComplete, completed, k)) {
                return false
            }
        }
        return true
    }

    fun dfs(
        route: MutableMap<Int, MutableList<Int>>,
        toFinish: MutableSet<Int>,
        finished: MutableSet<Int>,
        start: Int
    ): Boolean {
        if (toFinish.contains(start)) {
            return false
        }
        if (finished.contains(start)) {
            return true
        }
        if (route.containsKey(start)) {
            toFinish.add(start)
            for (end in route[start]!!) {
                if (!dfs(route, toFinish, finished, end)) {
                    return false
                }
            }
            toFinish.remove(start)
            finished.add(start)
        }
        return true
    }
}
